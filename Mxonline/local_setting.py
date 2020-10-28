# -*- coding: utf-8 -*-


LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mxonline',
        'HOST': '129.28.179.236',
        'PORT': 3306,
        'USER': 'chao',
        'PASSWORD': 'chao',
    }
}

AUTH_USER_MODEL = 'users.UserProfile'
