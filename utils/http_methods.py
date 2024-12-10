import allure
import requests
from utils.logger import setup_logger, start_logs, end_logs
from datetime import datetime


# Создаем логгер
logger = setup_logger()

class HttpMethods:
    '''Список Http методов'''

    headers = {'Content-Type': 'application/json'}
    cookie = {}

    @staticmethod
    def get(url):
        with allure.step('GET'):
            start_logs(logger, url, method='get')
            result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie, timeout=10)
            end_logs(logger, result)
            return result

    @staticmethod
    def post(url, body=None):
        with allure.step('POST'):
            start_logs(logger, url, method='post')
            result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie, timeout=10)
            end_logs(logger, result)
            return result

    @staticmethod
    def put(url, body=None):
        with allure.step('PUT'):
            start_logs(logger, url, method='put')
            result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie, timeout=10)
            end_logs(logger, result)
            return result

    @staticmethod
    def delete(url, body=None):
        with allure.step('DELETE'):
            start_logs(logger, url, method='delete')
            result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie, timeout=10)
            end_logs(logger, result)
            return result