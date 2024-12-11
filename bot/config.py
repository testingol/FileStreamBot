from os import environ as env

class Telegram:
    OWNER_ID = int(env.get("OWNER_ID", 5530237028))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "BotFather")
    SESSION_STRING = env.get("SESSION_STRING", "1234567:xyz")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -100123456789))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 24))

class Server:
    BASE_URL = env.get("BASE_URL", "http://127.0.0.1:8080")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 7860))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['stream_handler']
        },
        'hydrogram': {
            'level': 'INFO',
            'handlers': ['stream_handler']
        }
    }
}