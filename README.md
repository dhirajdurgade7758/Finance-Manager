# Finance Manager

Finance Manager is a Django-based web application that helps users manage their finances, including accounts, liabilities, investments, and subscriptions. Users can register, log in, and track their financial data in an organized way.

## Features

- User registration and authentication
- Manage multiple accounts
- Track liabilities (loans, debts, etc.)
- Track investments
- Manage subscriptions
- Monthly expense overview
- Secure and user-friendly interface

## Project Structure

```
FinanceManager/
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
fin_manager/
    __init__.py
    admin.py
    apps.py
    forms.py
    models.py
    tests.py
    urls.py
    views.py
    migrations/
    templates/
        expenses/
        fin_manager/
        registration/
manage.py
db.sqlite3
README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- [virtualenv](https://virtualenv.pypa.io/en/latest/) (recommended)

### Installation

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd Finance-Manager-main
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```sh
    pip install django
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser (optional, for admin access):**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

7. **Access the app:**
    Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage

- **Register** for a new account or **login** with existing credentials.
- Add and manage your accounts, liabilities, investments, and subscriptions.
- View your expenses grouped by month.
- Use the admin panel at `/admin/` for advanced management (if you are a superuser).

## File Overview

- [`FinanceManager/settings.py`](FinanceManager/settings.py): Project settings.
- [`fin_manager/models.py`](fin_manager/models.py): Database models for accounts, liabilities, investments, and subscriptions.
- [`fin_manager/views.py`](fin_manager/views.py): View functions for handling requests and rendering templates.
- [`fin_manager/forms.py`](fin_manager/forms.py): Django forms for user input.
- [`fin_manager/templates/`](fin_manager/templates/): HTML templates for the UI.
- [`fin_manager/urls.py`](fin_manager/urls.py): App-level URL routing.
- [`FinanceManager/urls.py`](FinanceManager/urls.py): Project-level URL routing.

## Database Models

- **Account**: Represents a user's financial account.
- **Liability**: Represents a financial liability (e.g., loan, debt).
- **Investments**: Represents an investment.
- **Subscription**: Represents a recurring subscription.

## Customization

- To add new features, edit or add models in [`fin_manager/models.py`](fin_manager/models.py) and create corresponding views and templates.
- Static files (CSS, JS) can be added in a `static/` directory and referenced in templates.

## Running Tests

To run tests, use:
```sh
python manage.py test
```

## License

This project is for educational purposes.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

**Developed with Django