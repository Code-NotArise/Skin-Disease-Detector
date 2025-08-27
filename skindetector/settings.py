from pathlib import Path
from django.conf import settings
from decouple import config, Csv

# ---------------------------------------------------
# Base directory of the Django project
# ---------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------------------------------
# SECURITY SETTINGS
# ---------------------------------------------------

# Secret key for cryptographic signing (keep it secret in production!)
SECRET_KEY = config('SECRET_KEY')

# Turn off DEBUG in production to avoid showing sensitive info
DEBUG = config('DEBUG', default=False, cast=bool)

# Hosts/domain names that are valid for this site
# Use specific domain names or IPs in production instead of '*'
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())

# ---------------------------------------------------
# MEDIA FILES CONFIGURATION (For user uploads)
# ---------------------------------------------------
MEDIA_URL = '/media/'                            # URL to access media files
MEDIA_ROOT = BASE_DIR / 'media'                  # Directory to save media files

# URL to redirect to for login-required views
LOGIN_URL = 'login'

# ---------------------------------------------------
# APPLICATIONS INSTALLED IN THIS PROJECT
# ---------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',                      # Admin interface
    'django.contrib.auth',                       # Authentication framework
    'django.contrib.contenttypes',               # Content type support
    'django.contrib.sessions',                   # Session framework
    'django.contrib.messages',                   # Messaging framework
    'django.contrib.staticfiles',                # Static file handling
    'detection',                                 # Custom app for skin disease detection
]

# ---------------------------------------------------
# MIDDLEWARE CONFIGURATION
# ---------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',               # Security enhancements
    'django.contrib.sessions.middleware.SessionMiddleware',        # Manage sessions
    'django.middleware.common.CommonMiddleware',                   # Common HTTP features
    'django.middleware.csrf.CsrfViewMiddleware',                   # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',     # Auth session handling
    'django.contrib.messages.middleware.MessageMiddleware',        # Message flashing
    'django.middleware.clickjacking.XFrameOptionsMiddleware',      # Clickjacking protection
]

# ---------------------------------------------------
# ROOT URL Configuration
# ---------------------------------------------------
ROOT_URLCONF = 'skindetector.urls'

# ---------------------------------------------------
# TEMPLATE ENGINE SETTINGS
# ---------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Optional: Add custom template directories here
        'APP_DIRS': True,  # Load templates from each app's "templates" folder
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',     # Required for admin
                'django.contrib.auth.context_processors.auth',    # User info in templates
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ---------------------------------------------------
# WSGI APPLICATION CONFIGURATION
# ---------------------------------------------------
WSGI_APPLICATION = 'skindetector.wsgi.application'

# ---------------------------------------------------
# DATABASE CONFIGURATION (Using MySQL)
# ---------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Database backend
        'NAME': config('DB_NAME', default='skin_db'),                     # Database name
        'USER': config('DB_USER', default='root'),                        # MySQL user
        'PASSWORD': config('DB_PASSWORD', default=''),            # MySQL password
        'HOST': config('DB_HOST', default='localhost'),                   # Database host
        'PORT': config('DB_PORT', default='3306'),                        # Default MySQL port
    }
}

# ---------------------------------------------------
# PASSWORD VALIDATION
# ---------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Enforce minimum length
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Avoid common passwords
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # Avoid fully numeric passwords
    },
]

# ---------------------------------------------------
# INTERNATIONALIZATION SETTINGS
# ---------------------------------------------------
LANGUAGE_CODE = 'en-us'     # Default language
TIME_ZONE = 'UTC'           # Default timezone
USE_I18N = True             # Enable internationalization
USE_TZ = True               # Use timezone-aware datetimes

# ---------------------------------------------------
# STATIC FILES CONFIGURATION (CSS, JavaScript, Images)
# ---------------------------------------------------
STATIC_URL = 'static/'      # URL to access static files (use collectstatic in production)

# ---------------------------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# ---------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Default type for auto-created primary keys
