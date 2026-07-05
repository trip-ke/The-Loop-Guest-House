# Loop Guest House System - Terminal Prompts

This guide gives you the step-by-step terminal prompts to create the foundation for a Python/Django guest house management system.

These commands are written for Bash on Linux/macOS. On Windows, use WSL or Git Bash after creating and activating the virtual environment.

Run these commands from the folder that should contain the project.

```bash
mkdir -p loop_guest_house
cd loop_guest_house
```

## 1. Create And Activate A Virtual Environment

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Upgrade packaging tools:

```bash
python -m pip install --upgrade pip setuptools wheel
```

## 2. Install Project Dependencies

```bash
pip install "Django>=5.2,<6.0" djangorestframework python-decouple dj-database-url Pillow psycopg2-binary django-cors-headers whitenoise gunicorn
```

Create `requirements.txt`:

```bash
pip freeze > requirements.txt
```

## 3. Create The Django Project

Create the Django project in the current folder:

```bash
python -m django startproject config .
```

Create the main app folders:

```bash
mkdir -p apps
mkdir -p templates static media docs tests scripts
touch apps/__init__.py
```

## 4. Create Django Apps

Create each business module. Django requires the destination folder to exist when you pass a custom app path, so create the folders first:

```bash
APPS="accounts guests rooms reservations checkin checkout payments invoices housekeeping inventory"

for app in $APPS; do
    mkdir -p "apps/$app"
    python manage.py startapp "$app" "apps/$app"
done
```

Because these apps live inside the `apps` package, update each generated app config so Django imports it correctly:

```bash
python - <<'PY'
from pathlib import Path

for path in Path("apps").glob("*/apps.py"):
    app_name = path.parent.name
    text = path.read_text()
    text = text.replace(f'name = "{app_name}"', f'name = "apps.{app_name}"')
    text = text.replace(f"name = '{app_name}'", f"name = 'apps.{app_name}'")
    path.write_text(text)
PY
```

## 5. Split Django Settings

Create the settings package:

```bash
mv config/settings.py /tmp/loop_guest_house_settings.py
mkdir -p config/settings
mv /tmp/loop_guest_house_settings.py config/settings/base.py
touch config/settings/__init__.py
touch config/settings/development.py config/settings/production.py
```

Update `manage.py` so it uses development settings:

```bash
python - <<'PY'
from pathlib import Path
path = Path("manage.py")
text = path.read_text()
text = text.replace("config.settings", "config.settings.development")
path.write_text(text)
PY
```

Update `config/wsgi.py`:

```bash
python - <<'PY'
from pathlib import Path
path = Path("config/wsgi.py")
text = path.read_text()
text = text.replace("config.settings", "config.settings.production")
path.write_text(text)
PY
```

Update `config/asgi.py`:

```bash
python - <<'PY'
from pathlib import Path
path = Path("config/asgi.py")
text = path.read_text()
text = text.replace("config.settings", "config.settings.development")
path.write_text(text)
PY
```

## 6. Configure Environment Variables

Create `.env`:

```bash
touch .env
```

Add development values to `.env`:

```bash
cat > .env <<'EOF'
SECRET_KEY=change-this-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
EOF
```

## 7. Configure `base.py`

Replace `config/settings/base.py` with this:

```python
from pathlib import Path
from decouple import config, Csv
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config("SECRET_KEY", default="unsafe-development-key")
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1,localhost", cast=Csv())

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "apps.accounts.apps.AccountsConfig",
    "apps.guests.apps.GuestsConfig",
    "apps.rooms.apps.RoomsConfig",
    "apps.reservations.apps.ReservationsConfig",
    "apps.checkin.apps.CheckinConfig",
    "apps.checkout.apps.CheckoutConfig",
    "apps.payments.apps.PaymentsConfig",
    "apps.invoices.apps.InvoicesConfig",
    "apps.housekeeping.apps.HousekeepingConfig",
    "apps.inventory.apps.InventoryConfig",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Nairobi"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
```

## 8. Configure Development And Production Settings

Add this to `config/settings/development.py`:

```python
from .base import *

DEBUG = True
```

Add this to `config/settings/production.py`:

```python
from .base import *

DEBUG = False

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
```

## 9. Configure URLs

Update `config/urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 10. Create A Professional README

````bash
cat > README.md <<'EOF'
# Loop Guest House Management System

A Django-based guest house management system for managing guests, rooms, reservations, check-in, checkout, payments, invoices, housekeeping, and inventory.

## Main Modules

- Accounts and staff users
- Guest records
- Rooms and room status
- Reservations
- Check-in and checkout
- Payments
- Invoices
- Housekeeping
- Inventory

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
EOF
````

## 11. Run Initial Database Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

## 12. Create Admin User

```bash
python manage.py createsuperuser
```

## 13. Run The Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/admin/
```

## 14. Suggested Model Development Order

Build the system in this order:

1. `accounts` - staff users, roles, permissions
2. `guests` - guest profile, contacts, identification
3. `rooms` - room type, room number, status, price
4. `reservations` - booking dates, guest, room, status
5. `checkin` - arrival records, assigned room, check-in time
6. `checkout` - departure records, charges summary
7. `payments` - payment method, amount, transaction reference
8. `invoices` - invoice number, invoice lines, tax, totals
9. `housekeeping` - cleaning tasks, room condition, staff assigned
10. `inventory` - stock items, quantities, restock alerts

## 15. Recommended Next Terminal Prompts

After the foundation is working, create model files and admin registrations one app at a time:

```bash
python manage.py makemigrations accounts guests rooms reservations
python manage.py migrate
python manage.py runserver
```

Run tests:

```bash
python manage.py test
```

Collect static files for production:

```bash
python manage.py collectstatic --noinput
```

## 16. Final Target Project Structure

```text
loop_guest_house/
├── manage.py
├── requirements.txt
├── README.md
├── .env
├── config/
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── settings/
│       ├── __init__.py
│       ├── base.py
│       ├── development.py
│       └── production.py
├── apps/
│   ├── __init__.py
│   ├── accounts/
│   ├── guests/
│   ├── rooms/
│   ├── reservations/
│   ├── checkin/
│   ├── checkout/
│   ├── payments/
│   ├── invoices/
│   ├── housekeeping/
│   └── inventory/
├── templates/
├── static/
├── media/
├── docs/
├── tests/
└── scripts/
```
