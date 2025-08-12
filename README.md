# Django Blog + Portfolio

A simple **Django** site that combines a personal **blog** with a **portfolio**. It includes a public-facing blog with the ability to comment, and a deprecated portfolio page for displaying my projects.

## Features

* Blog posts + Commenting (CRUD)
* Projects/Portfolio listing
* About/Home pages
* Bootstrap CSS

## Quick Start

```bash
# 1) Clone
git clone https://github.com/Reuvi/Django-Blog-Portfolio
cd Django-Blog-Portfolio

# 2) (Optional) Create & activate a virtualenv
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3) Install dependencies
pip install -r requirements.txt  # if not present: pip install django

# 4) Migrate DB and create an admin user
python manage.py migrate
python manage.py createsuperuser

# 5) Run
python manage.py runserver
```

## Configuration

* Create a `.env` or export env vars for:

  * `SECRET_KEY` (required)
  * `DEBUG` (set to `False` in production)
  * `ALLOWED_HOSTS` (e.g., `example.com,localhost,127.0.0.1`)
* Update `DATABASES` in `settings.py` if not using SQLite.

## Admin

* Go to **/admin/** and sign in with the superuser created during Quick Start.
* Create blog posts and manage comments from the admin and/or home page with special admin endpoints.

## Project Structure

```
Django-Blog-Portfolio/
├─ app/                     # blog/portfolio app (views, models, urls, templates)
├─ templates/               # base.html, index.html, blog templates
├─ static/                  # CSS/JS; Bootstrap included
├─ media/                   # user-uploaded files (if enabled)
├─ manage.py
└─ requirements.txt
```

## Deploy

* Set environment variables: `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`.

* Run migrations: `python manage.py migrate`.

* Start with a WSGI server (e.g., `gunicorn project.wsgi:application`) behind Nginx, or deploy to a platform like Render/Railway/Fly.io.
