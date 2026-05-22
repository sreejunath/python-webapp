from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost').split(',')

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'college_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'college_site.wsgi.application'

DB_ENGINE = config('DB_ENGINE', default='sqlite')

if DB_ENGINE == 'mysql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME':     config('DB_NAME'),
            'USER':     config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST':     config('DB_HOST', default='localhost'),
            'PORT':     config('DB_PORT', default='3306'),
            'OPTIONS':  {'charset': 'utf8mb4'},
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / config('DB_NAME', default='db.sqlite3'),
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

JAZZMIN_SETTINGS = {
    "site_title": "College Admin",
    "site_header": "DEMO METCA",
    "site_brand": "METCA Admin",
    "welcome_sign": "Welcome, College Staff",
    "copyright": "DEMO METCA",
    "topmenu_links": [
        {"name": "View Website", "url": "/", "new_window": True},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "auth":                       "fas fa-users-cog",
        "auth.user":                  "fas fa-user",
        "main.course":                "fas fa-book",
        "main.faculty":               "fas fa-chalkboard-teacher",
        "main.notice":                "fas fa-bell",
        "main.galleryimage":          "fas fa-images",
        "main.foundermessage":        "fas fa-quote-left",
        "main.admissionapplication":  "fas fa-file-alt",
        "main.contactmessage":        "fas fa-envelope",
        "main.collegesettings":       "fas fa-cog",
    },
    "default_icon_parents":  "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active":  True,
    "changeform_format":     "horizontal_tabs",
    "order_with_respect_to": [
        "main.collegesettings",
        "main.course",
        "main.faculty",
        "main.notice",
        "main.galleryimage",
        "main.foundermessage",
        "main.admissionapplication",
        "main.contactmessage",
    ],
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text":          False,
    "footer_small_text":          False,
    "body_small_text":            False,
    "brand_small_text":           False,
    "brand_colour":               "navbar-primary",
    "accent":                     "accent-primary",
    "navbar":                     "navbar-dark",
    "no_navbar_border":           False,
    "navbar_fixed":               True,
    "layout_boxed":               False,
    "footer_fixed":               False,
    "sidebar_fixed":              True,
    "sidebar":                    "sidebar-dark-primary",
    "sidebar_nav_small_text":     False,
    "sidebar_disable_expand":     False,
    "sidebar_nav_child_indent":   True,
    "sidebar_nav_compact_style":  False,
    "sidebar_nav_legacy_style":   False,
    "sidebar_nav_flat_style":     False,
    "theme":                      "default",
}