from datetime import timedelta
from rest_framework_simplejwt import settings as jwt_settings

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'AUTH_TOKEN_CLASSES': ['rest_framework_simplejwt.tokens.AccessToken'],
    
    'SIMPLE_JWT': {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),  # Duration of access token (5 minutes)
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),  # Duration of refresh token (1 day)
    "ROTATE_REFRESH_TOKENS": False,              # Automatically refresh tokens (disabled)
    "BLACKLIST_AFTER_ROTATION": False,           # Blacklist old refresh tokens (disabled)
    "UPDATE_LAST_LOGIN": False,                  # Update user's last login on login (disabled)
   
    }
}


