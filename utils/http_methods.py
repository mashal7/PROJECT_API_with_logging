import allure
import requests
from utils.custom_logger import CustomLogger
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
            CustomLogger.add_request(url, method='get')
            start_logs(logger, url, method='get')
            result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie, timeout=10)
            end_logs(logger, result)
            CustomLogger.add_response(result)
            return result

    @staticmethod
    def post(url, body=None):
        with allure.step('POST'):
            CustomLogger.add_request(url, method='post')
            start_logs(logger, url, method='post')
            result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie, timeout=10)
            end_logs(logger, result)
            CustomLogger.add_response(result)
            return result

    @staticmethod
    def put(url, body=None):
        with allure.step('PUT'):
            CustomLogger.add_request(url, method='put')
            start_logs(logger, url, method='put')
            result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie, timeout=10)
            end_logs(logger, result)
            CustomLogger.add_response(result)
            return result

    @staticmethod
    def delete(url, body=None):
        with allure.step('DELETE'):
            CustomLogger.add_request(url, method='delete')
            start_logs(logger, url, method='delete')
            result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie, timeout=10)
            end_logs(logger, result)
            CustomLogger.add_response(result)
            return result