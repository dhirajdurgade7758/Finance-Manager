from django import forms
from .models import Liability, Investments

class LiabilityForm(forms.ModelForm):
    class Meta:
        model = Liability
        fields = ['name', 'amount', 'interest_rate', 'end_date']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'interest_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
