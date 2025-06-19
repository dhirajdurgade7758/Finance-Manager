from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from fin_manager import models
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, F
from django.views.generic import TemplateView
from .models import Account, Liability
from .forms import LiabilityForm
from django.views.generic.edit import FormView
from django.views.generic import ListView


# Create your views here.

# @login_required(login_url='/signin')

def home(request):
    return render(request, 'fin_manager/home.html', {'user': request.user})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            return redirect('home')  # Change 'home' to your desired URL
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class ExpenseListView(FormView):
    template_name = 'expenses/expense_list.html'
    form_class = LiabilityForm
    success_url = '/expenses/'  # Update this with the correct URL

    def form_valid(self, form):
        # Retrieve the user's account
        account, _ = Account.objects.get_or_create(user=self.request.user)
        
        # Create a new liability instance and link it to the user's account
        liability = Liability(
            name=form.cleaned_data['name'],
            amount=form.cleaned_data['amount'],
            interest_rate=form.cleaned_data['interest_rate'],
            end_date=form.cleaned_data['end_date'],
            user=self.request.user
        )
        liability.save()
        account.liability_list.add(liability)
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        # Retrieve user's account data and related liabilities
        accounts = Account.objects.filter(user=user)
        print(accounts)
        # Create a dictionary to store expense data grouped by month
        expense_data = {}

        for account in accounts:
            liabilities = account.liability_list.all()
            for liability in liabilities:
                year_month = liability.end_date.strftime('%Y-%m')

                if year_month not in expense_data:
                    expense_data[year_month] = []

                expense_data[year_month].append({
                    'name': liability.name,
                    'amount': liability.amount,
                    'end_date': liability.end_date,
                })
        
        context['expense_data'] = expense_data
        return context
