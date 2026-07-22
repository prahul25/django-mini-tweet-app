# Django Mini Tweet App

A lightweight Twitter-like microblogging app built with Django 6.0.7, Tailwind CSS v4, and Alpine.js.

![Django](https://img.shields.io/badge/Django-6.0.7-092E20?logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-4.3-38B2AC?logo=tailwind-css&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

- **Tweet CRUD** — Create, read, edit, delete tweets with 240-character limit
- **Image upload** — Optional photo per tweet with drag-drop zone
- **Responsive grid feed** — 1/2/3 columns (mobile/tablet/desktop)
- **Dark/light mode** — Persisted in localStorage, Tailwind class-based
- **Live character counter** — Circular progress with color warnings
- **Image preview modal** — Click filename or eye icon to view full-size
- **Auth** — Register, login, logout with `@login_required` guards
- **Clean UI** — Indigo/slate palette, consistent dark mode support

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django 6.0.7 |
| Frontend | Tailwind CSS v4.3, Alpine.js 3.x |
| Database | SQLite (dev) |
| Icons | Inline SVG |

## Quick Start

```bash
# Clone
git clone <repo-url>
cd django-mini-tweet-app/tweet_app

# Create & activate venv
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install deps
pip install -r requirements.txt

# Migrate DB
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run dev server
python manage.py runserver
```

Open `http://127.0.0.1:8000/tweet/`

### Tailwind CSS (dev)

```bash
# Watch mode (auto-rebuild on template changes)
python manage.py tailwind start

# One-off production build
python manage.py tailwind build
```

## Commands

| Command | Description |
|---------|-------------|
| `python manage.py runserver` | Start dev server |
| `python manage.py migrate` | Apply migrations |
| `python manage.py makemigrations` | Create new migrations |
| `python manage.py createsuperuser` | Create admin user |
| `python manage.py tailwind start` | Tailwind watch mode |
| `python manage.py tailwind build` | Production CSS build |
| `python manage.py test` | Run tests (none yet) |

## Project Structure

```
django-mini-tweet-app/
├── AGENTS.md                    # Agent instructions
├── README.md
├── requirements.txt
├── tweet_app/                   # Django project root
│   ├── manage.py
│   ├── db.sqlite3
│   ├── media/photos/            # Uploaded tweet images
│   ├── tweet_app/               # Project config
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py / asgi.py
│   │   └── ...
│   ├── tweet/                   # Main tweet app
│   │   ├── models.py            # Tweet model
│   │   ├── views.py             # CRUD + auth views
│   │   ├── forms.py             # TweetForm + UserRegisterationForm
│   │   ├── urls.py              # tweet/ routes
│   │   ├── templates/
│   │   │   ├── tweet_list.html  # Grid feed
│   │   │   ├── tweet_form.html  # Create/edit with preview modal
│   │   │   └── tweet_confirm_delete.html
│   │   └── ...
│   ├── theme/                   # Tailwind CSS app
│   │   └── static_src/src/styles.css
│   └── templates/
│       ├── layout.html          # Base + navbar + dark toggle
│       └── registration/        # Auth templates
│           ├── login.html
│           ├── register.html
│           └── logged_out.html
```

## Auth Flow

```
Register (POST /tweet/register/) 
  → auto-login → redirect /tweet/

Login (GET/POST /accounts/login/)
  → redirect /tweet/

Logout (POST /accounts/logout/)
  → redirect /accounts/login/

@login_required protects:
  /tweet/create/
  /tweet/<id>/edit/
  /tweet/<id>/delete/
```

## Known Issues

See `AGENTS.md` — current bugs:
- `TweetForm` originally didn't inherit `ModelForm`
- `tweet.save` missing `()` in create view
- `tweet_edit` double-save
- Edit/delete URLs missing `<tweet_id>` parameter

## License

MIT — free to use, modify, distribute.