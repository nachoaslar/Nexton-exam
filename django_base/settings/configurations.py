from datetime import timedelta
from django_base.settings.environment_variables import BASE_DIR


# <-------------- General configurations -------------->
APP_NAME = "Django Base"
USE_DEBUG_TOOLBAR = False

# <-------------- Auth configurations -------------->
USE_EMAIL_FOR_AUTHENTICATION = False
USE_JWT = False

PASSWORD_CHANGE_BY_EMAIL = False

PASSWORD_RECOVERY_TOKEN_TYPE = "link"  # link | code
PASSWORD_RECOVERY_TOKEN_EXPIRE_AT = timedelta(minutes=30)
PASSWORD_RECOVERY_TOKEN_LENGTH = 25 if PASSWORD_RECOVERY_TOKEN_TYPE == "link" else 6

# <-------------- Lenguaje and timezone settings -------------->
LOCALE_PATHS = [
    f"{BASE_DIR}/locale",
]

LANGUAGES = [
    ("en", "English"),
]


# <-------------- Global places env settings -------------->
GLOBAL_PLACES = {
    "INCLUDE_LOCATION": False,
    "LOCATION_SCOPE": "state",
    "INCLUDE_EXPANDED_COUNTRY": False,
}


# <-------------- Async settings --------------> #tmp until cookiecutter update
USE_CELERY = False
USE_WEB_SOCKET = False
