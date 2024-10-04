import logging, os
from datetime import datetime

# Настройка логирования
def setup_logger():
    # Создаем логгер
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Создаем обработчик для записи логов в файл
    handler = logging.FileHandler(f'logs/log_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log', 'w')
    handler.setLevel(logging.DEBUG)

    # Форматирование логов
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(handler)

    return logger

def start_logs(logger, url, method):
    '''Логи перед началом теста'''

    test_name = os.environ.get('PYTEST_CURRENT_TEST')
    logger.info(f'-----\nTest: {test_name}\nRequest method: {method}\nRequest URL: {url}\n')


def end_logs(logger, result):
    '''Логи после окончания теста'''

    cookies = dict(result.cookies)
    headers = dict(result.headers)
    logger.info(f'Response code: {result.status_code}\nResponse text: {result.text}\nResponse headers: {headers}\nResponse cookies: {cookies}\n')