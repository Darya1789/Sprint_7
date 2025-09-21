import pytest
import requests
import allure
import json
from urls import Urls
from data import Order

class TestCreateOrder:

    @allure.title('Проверка возможности создания задказа с различными варантами цветов')
    @allure.description("Проверяем возможность создать заказ с возможностью выбора цветов: ['BLACK'], ['GREY'], ['BLACK', 'GREY'] и без выбора цвета")
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order(self, color):
        with allure.step('Заполняем заказ данными'):
            order = Order.order_data
        with allure.step('Добавляем к данным заказа выбор цвета'):
            order['color'] = color
        with allure.step('Преобразуем данным о заказе в формат json для последующей передачи в запрос'):
            order = json.dumps(order)
        with allure.step('Создаем заказ'):
            response = requests.post(Urls.URL_CREATE_ORDER, data = order)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 201, \
            f'Ожидаемый код ответа: 201, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем, что сообщение ответа содержи5тася слово "track'):
            assert 'track' in response.json(), \
            f'Ожимаем "track" в сообщении ответа: {response.json()}'
        with allure.step('Проверяем, что номер трека является числом int'):
            assert isinstance(response.json()['track'], int), \
            f'Ожидаем число, фактическое сообщение ответа: {response.json()}'
        with allure.step('Отменяем созданный заказ'):
            requests.put(Urls.URL_CANCEL_ORDER, params={'track': response.json()['track']})