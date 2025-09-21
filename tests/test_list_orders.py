import requests
import allure
from urls import Urls

class TestListOrder:

    @allure.title('Проверка списка заказов')
    @allure.description('Отправляем запрос на получение всех заказов')
    def test_get_list_orders(self):
        with allure.step('Отправляем запрос на получение списка всех заказов'):
            response = requests.get(Urls.URL_LIST_ORDERS)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 200
            f'Ожидаемый код ответа: 200, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем наличие "orders", "pageInfo", "availableStations" в сообщении ответа '):
            assert 'orders' in response.json() and 'pageInfo' in response.json() and 'availableStations' in response.json(), \
            f'Ответ: {response.json()}'