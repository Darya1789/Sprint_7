import pytest
import requests
import allure
import json
from urls import Urls
from data import Order, RequestsAnswer

class TestAcceptOrder:

    @allure.title('Проверка принятия заказа')
    @allure.description('Создаем курьера, создаем заказ, принимаем заказ по id заказа и id курьера')
    def test_accept_order_valid_id_order_and_courier(self, create_order_and_return_id, login_courier_and_return_id):
        with allure.step('Получаем id курьера'):
            id_courier = login_courier_and_return_id
        with allure.step('Получаем id заказа'):
            id_order = create_order_and_return_id
        with allure.step('Получаем url для принятия заказа'):
            url_for_accept_order = f'{Urls.URL_ACCEPT_ORDER}{id_order}'
        with allure.step('Отправляем запрос на прнятие заказа'):
            response = requests.put(url_for_accept_order, params={'courierId' : id_courier}) 
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 200, \
            f'Ожидаемый код ответа: 200, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем сообщение ответа'):
            assert response.json() == RequestsAnswer.answer_accept_order_valid, \
            f'Ожидаемое сообщение ответа: {RequestsAnswer.answer_accept_order_valid}, Фактическое сообщение: {response.json()}'

    @allure.title('Проверка принятия заказа без id курьера')
    @allure.description('Создаем заказ, принимаем заказ по id заказа и без id курьера')
    def test_accept_order_without_id_courier(self, create_order_and_return_id): 
        with allure.step('Получаем id заказа'):
            id_order = create_order_and_return_id
        with allure.step('Получаем url для принятия заказа'):
            url_for_accept_order = f'{Urls.URL_ACCEPT_ORDER}{id_order}'
        with allure.step('Отправляем запрос на прнятие заказа'):
            response = requests.put(url_for_accept_order) 
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 400, \
            f'Ожидаемый код ответа: 400, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем сообщение ответа'):
            assert response.json() == RequestsAnswer.answer_accept_order_witout_id_order_id_courier, \
            f'Ожидаемое сообщение ответа: {RequestsAnswer.answer_accept_order_witout_id_order_id_courier}, Фактическое сообщение: {response.json()}'

    @allure.title('Проверка принятия заказа без id заказа')
    @allure.description('Создаем курьера, принимаем заказ id курьера без id заказа')
    def test_accept_order_without_id_order(self, login_courier_and_return_id):
        with allure.step('Получаем id курьера'):
            id_courier = login_courier_and_return_id
        with allure.step('Отправляем запрос на прнятие заказа'):
            response = requests.put(Urls.URL_ACCEPT_ORDER, params={'courierId' : id_courier}) 
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 400, \
            f'Ожидаемый код ответа: 400, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем сообщение ответа'):
            assert response.json() == RequestsAnswer.answer_accept_order_witout_id_order_id_courier, \
            f'Ожидаемое сообщение ответа: {RequestsAnswer.answer_accept_order_witout_id_order_id_courier}, Фактическое сообщение: {response.json()}'
        
    @allure.title('Проверка принятия заказа с несуществующим id курьера')
    @allure.description('Создаем заказ, принимаем заказ по id заказа и несуществующему id курьера')
    def test_accept_order_with_invalid_id_courier(self, create_order_and_return_id):
        with allure.step('Получаем несуществующий id курьера'):
            id_courier = 987654321
        with allure.step('Получаем id заказа'):
            id_order = create_order_and_return_id
        with allure.step('Получаем url для принятия заказа'):
            url_for_accept_order = f'{Urls.URL_ACCEPT_ORDER}{id_order}'
        with allure.step('Отправляем запрос на прнятие заказа'):
            response = requests.put(url_for_accept_order, params={'courierId' : id_courier}) 
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 404, \
            f'Ожидаемый код ответа: 404, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем сообщение ответа'):
            assert response.json() == RequestsAnswer.answer_accept_order_with_invalid_id_courier, \
            f'Ожидаемое сообщение ответа: {RequestsAnswer.answer_accept_order_with_invalid_id_courier}, Фактическое сообщение: {response.json()}'


    @allure.title('Проверка принятия заказа с несуществующим id заказа')
    @allure.description('Создаем курьера, принимаем заказ по несуществующему id заказа и id курьера')
    def test_accept_order_with_invalid_id_order(self, login_courier_and_return_id):
        with allure.step('Получаем id курьера'):
            id_courier = login_courier_and_return_id
        with allure.step('Получаем несуществующий id заказа'):
            id_order = 987654321
        with allure.step('Получаем url для принятия заказа'):
            url_for_accept_order = f'{Urls.URL_ACCEPT_ORDER}{id_order}'
        with allure.step('Отправляем запрос на прнятие заказа'):
            response = requests.put(url_for_accept_order, params={'courierId' : id_courier}) 
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 404, \
            f'Ожидаемый код ответа: 404, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем сообщение ответа'):
            assert response.json() == RequestsAnswer.answer_accept_order_with_invalid_id_order, \
            f'Ожидаемое сообщение ответа: {RequestsAnswer.answer_accept_order_with_invalid_id_order}, Фактическое сообщение: {response.json()}'
