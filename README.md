# Loop Guest House Management System

A Django 5 guest house management system for learning and building incrementally.

## Current Features

- Staff login and admin access
- Dashboard summary
- Guests CRUD with search and guest history
- Room types and rooms
- Reservations with double-booking validation
- Payments
- PDF and Excel reservation reports
- DRF API for guests, room types, rooms, and reservations

## Local Setup

```bash
source .venv/bin/activate
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Development login:

```text
username: admin
password: Admin12345!
```

## Useful Commands

```bash
python manage.py check
python manage.py test
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## PostgreSQL

For PostgreSQL, create a database and update `.env`:

```text
DATABASE_URL=postgres://USER:PASSWORD@localhost:5432/loop_guest_house
```
