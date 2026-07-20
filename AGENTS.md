# AGENTS.md

## Project

Django 6.0.7 mini tweet app with Tailwind CSS (v4.3 via `django-tailwind`). Python 3.13. SQLite. Single custom app: `tweet`. Theme app (`theme`) is just the Tailwind CSS integration.

## Structure

The Django project root is `tweet_app/` (contains `manage.py`). The settings module is `tweet_app/settings.py`. All custom code lives under `tweet_app/`.

```
tweet_app/
  manage.py
  tweet_app/        ← project config (settings, root urls, wsgi/asgi)
  tweet/            ← main app (models, views, forms, urls, templates)
  theme/            ← Tailwind CSS app (static_src/ has source CSS)
  templates/        ← project-level templates (layout.html)
  media/photos/     ← user-uploaded images
```

## Commands

```bash
# All commands run from tweet_app/ (where manage.py lives)
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
python manage.py tailwind start   # starts Tailwind CSS watcher (separate terminal)
python manage.py tailwind build   # one-off Tailwind build
python manage.py test             # no tests written yet
```

No linting, formatting, or type-checking tools are configured.

## Known Issues (as of current state)

- `tweet/forms.py`: `TweetForm` does not inherit from `forms.ModelForm` — will fail at runtime.
- `tweet/views.py:21`: `tweet.save` is missing parentheses — tweet creation silently fails.
- `tweet/urls.py` only routes `index` — `tweet_list`, `tweet_create`, `tweet_edit`, `tweet_delete` views exist but have no URL patterns.
- Views reference templates (`tweet_list.html`, `tweet_form.html`, `tweet_edit.html`, `tweet_confirm_delete.html`) that do not exist.
- `settings.py` defines `STATIC_URL` twice; second definition overrides the first.
- `db.sqlite3` is tracked in git despite `.gitignore` rule (committed before ignore was effective).

## Conventions

- No established code style beyond default Django.
- No CI, no pre-commit hooks, no README yet.
- Templates use Tailwind CSS utility classes. Base layout is `templates/layout.html`.
