"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from django.urls import reverse_lazy

######################################################################
# General
######################################################################
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-l%q$xgfkid)qa2r)#y%2x$k*&6o58w2#ir39*$3#pysvhu22w_"

DEBUG = True


ROOT_URLCONF = "main.urls"

WSGI_APPLICATION = "main.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

######################################################################
# Domains
######################################################################
# ALLOWED_HOSTS = environ.get("ALLOWED_HOSTS", "localhost").split(",")

# CSRF_TRUSTED_ORIGINS = environ.get(
#     "CSRF_TRUSTED_ORIGINS", "http://localhost:8000"
# ).split(",")


######################################################################
# Apps
######################################################################

INSTALLED_APPS = [
    "accounts",
    "unfold",
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    # "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history",  # optional, if django-simple-history package is used
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_browser_reload",
    "django_filters",
    "django_admin_multiple_choice_list_filter",
    "djmoney",
    # "compressor",
    "lead",
    "place",
    "department",
    "nested_admin",
    "sales",
]


######################################################################
# Middleware
######################################################################

MIDDLEWARE = [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

######################################################################
# Sessions
######################################################################
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

######################################################################
# Templates
######################################################################
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


######################################################################
# Databases
######################################################################
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


######################################################################
# Authentication
######################################################################

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LOGIN_URL = "admin:login"

LOGIN_REDIRECT_URL = reverse_lazy("admin:index")

######################################################################
# Localization
######################################################################

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

######################################################################
# Django Money
######################################################################
CURRENCIES = ("USD", "EUR")
CURRENCY_CHOICES = [("USD", "USD $"), ("EUR", "EUR €")]


######################################################################
# Static
######################################################################

# COMPRESS_ROOT = BASE_DIR / "static"

# COMPRESS_ENABLED = True

# STATICFILES_FINDERS = ("compressor.finders.CompressorFinder",)
STATIC_URL = "http://127.0.0.1:5500/main/static/"
STATIC_ROOT = BASE_DIR / "static"
# STATICS_DIRS = [BASE_DIR / "static"]


from django.templatetags.static import static
from .unfold_settings import UNFOLD

UNFOLD = {
    **UNFOLD,
    "STYLES": [
        lambda request: static("css/styles.css"),
    ],
}
