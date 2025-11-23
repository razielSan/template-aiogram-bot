from aiogram import Bot, Dispatcher

from bot.config.bot_settings import BotSettings
from app_utils.logging import init_loggers, setup_bot_logging, get_loggers
from settings.response import app_settings
from core.logging import LoggerStorage


# Создаем хранилище логгеров
logging_data = LoggerStorage()

# Получаем настройки бота
bot_settings = BotSettings()

# Создаем бота и диспетчер
bot: Bot = Bot(token=bot_settings.TOKEN)
dp: Dispatcher = Dispatcher()


# Инициализируем логи
init_loggers(
    bot_name=bot_settings.BOT_NAME,
    setup_bot_logging=setup_bot_logging,
    log_format=app_settings.LOG_FORMAT,
    date_format=app_settings.DATE_FORMAT,
    base_path=app_settings.PATH_LOG_FOLDER,
    log_data=logging_data,
)

main_logger = get_loggers(
    router_name=bot_settings.BOT_NAME,
    logging_data=logging_data,
)