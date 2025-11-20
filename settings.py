import os
from pathlib import Path

# مسار المشروع الأساسي
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key-here'   # غيّرها لاحقاً

DEBUG = True   # أثناء التطوير
ALLOWED_HOSTS = ['*']


# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات النظام
    'accounts',   # تسجيل دخول + مستخدمين + أدوار
    'pos',        # نظام POS + منتجات + فواتير
]


# الوسائط الوسطية
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'pos_system.urls'

# إعدادات القوالب (templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # مجلد الصفحات
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


WSGI_APPLICATION = 'pos_system.wsgi.application'



# 📌 إعدادات MySQL — غيّر البيانات حسب جهازك
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pos_db',      # اسم قاعدة البيانات
        'USER': 'root',        # المستخدم
        'PASSWORD': '',        # كلمة المرور
        'HOST': 'localhost',   # السيرفر
        'PORT': '3306',        # المنفذ الافتراضي
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}



# اللغة والوقت
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True



# الملفات الثابتة Static
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# ملفات الميديا
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# إعادة التوجّه بعد تسجيل الدخول
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'
