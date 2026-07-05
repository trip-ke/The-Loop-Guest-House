# Running The Loop Guest House System

Use these prompts from the project root:

```bash
cd "/home/trip/Documents/sharp/The Loop Guest House"
```

## 1. Activate The Virtual Environment

```bash
source .venv/bin/activate
```

## 2. Install Dependencies

Run this if dependencies are missing or after pulling new changes:

```bash
pip install -r requirements.txt
```

## 3. Check The Project

```bash
python manage.py check
```

## 4. Apply Database Migrations

```bash
python manage.py migrate
```

## 5. Create An Admin User

Skip this if you already have a user.

```bash
python manage.py createsuperuser
```

Current development login already created:

```text
username: admin
password: Admin12345!
```

## 6. Run The Development Server

Normal command:

```bash
python manage.py runserver
```

If the file watcher causes permission issues in this workspace, use:

```bash
python manage.py runserver 127.0.0.1:8000 --noreload
```

Open:

```text
http://127.0.0.1:8000/
```

Admin:

```text
http://127.0.0.1:8000/admin/
```

API:

```text
http://127.0.0.1:8000/api/
```

## 7. Run Tests

```bash
python manage.py test
```

## 8. Collect Static Files

Use this before production-style serving:

```bash
python manage.py collectstatic --noinput
```

## 9. Optional PostgreSQL Setup

The project currently uses SQLite through `.env`:

```text
DATABASE_URL=sqlite:///db.sqlite3
```

To use PostgreSQL, create a database and update `.env`:

```text
DATABASE_URL=postgres://USER:PASSWORD@localhost:5432/loop_guest_house
```

Then run:

```bash
python manage.py migrate
```
