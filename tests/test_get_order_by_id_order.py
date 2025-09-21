import pytest
import requests
import allure
import json
from urls import Urls
from data import Order, RequestsAnswer

class TestGetOrder:

    @allure.title('Проверка получения информации о заказе по id заказа')
    @allure.description('Создаем заказ, получаем id заказа, пытаемя получить информацию о заказе по id заказа')
    def test_get_order_by_id_order(self, create_order_and_return_id):
        with allure.step('Создаем и получаем id заказа'):
            id_order = create_order_and_return_id
        with allure.step('Отправляем запрос на получене заказа по id'):
            response = requests.get(Urls.URL_GET_ORDER_BY_ID, params={'t' : id_order})
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 200, \
            f'Ожидаемый код ответа: 200, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем наличие "order" в ответе'):
            assert 'order' in response.json(), \
            f'Полученное сообщение ответа: {response.json()}'

    @allure.title('Проверка получения информации о заказе по id заказа')
    @allure.description('Создаем заказ, получаем id заказа, пытаемя получить информацию о заказе по id заказа')
    def test_get_order_by_id_order_without_id_order(self):
        with allure.step('Отправляем запрос на получене заказа без id'):
            response = requests.get(Urls.URL_GET_ORDER_BY_ID)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 400, \
            f'Ожидаемый код ответа: 400, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем сообщение об ошибке'):
            assert RequestsAnswer.answer_get_order_without_id == response.json(), \
            f'Ожидаемое сообщение: {RequestsAnswer.answer_get_order_without_id}, Полученное сообщение ответа: {response.json()}'

    @allure.title('Проверка получения информации о заказе по несуществующему id заказа')
    @allure.description('Создаем несуществующий id заказа, пытаемя получить информацию о заказе ')
    def test_get_order_by_id_order_with_invalid_id(self):
        with allure.step('Создаем несуществующий id заказа'):
            id_order = 987654321
        with allure.step('Отправляем запрос на получене заказа по id'):
            response = requests.get(Urls.URL_GET_ORDER_BY_ID, params={'t' : id_order})
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 404, \
            f'Ожидаемый код ответа: 404, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем сообщение об ошибке'):
            assert RequestsAnswer.answer_get_order_with_invalid_id == response.json(), \
            f'Ожидаемое сообщение: {RequestsAnswer.answer_get_order_with_invalid_id}, Полученное сообщение ответа: {response.json()}'
