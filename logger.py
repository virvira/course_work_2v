import logging

api_logger = logging.getLogger("api_logger")
api_logger.setLevel(logging.INFO)
# Cоздаем обработчик
api_logger_handler = logging.FileHandler('logs/app.log')
api_logger_handler.setLevel(logging.INFO)
api_logger.addHandler(api_logger_handler)
# Создаем новое форматирование (объект класса Formatter)
api_logger_format = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
# Применяем форматирование к обработчику
api_logger_handler.setFormatter(api_logger_format)
