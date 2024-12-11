from hydrogram import Client
from logging import getLogger
from logging.config import dictConfig
from .config import Telegram, LOGGER_CONFIG_JSON

dictConfig(LOGGER_CONFIG_JSON)

version = 1.8
logger = getLogger('bot')

TelegramBot = Client(
    name = 'bot',
    session_string = Telegram.SESSION_STRING,
    plugins = {'root': 'bot/plugins'},
    sleep_threshold = -1,
    max_concurrent_transmissions = 10,
)
