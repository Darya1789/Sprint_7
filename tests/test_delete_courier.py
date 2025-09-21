import requests
import allure
from urls import Urls
from data import RequestsAnswer
from helper import GenerateNewCourier

class TestDeleteCourier:

    @allure.title('Проверка удаления существующего курьера')
    @allure.description('Создаем курьера, логиимся и удаляем созданого курьера')
    def test_delete_exist_courier(self):
        with allure.step('Генерируем валидные данные для создания курьера'):
            courier = GenerateNewCourier.register_new_courier_and_return_login_password()
        with allure.step('Создаем курьера'):
            requests.post(Urls.URL_CREATE_COURIER, data = courier[0])
        with allure.step('Логинимся'):
            response_login = requests.post(Urls.URL_LOGIN_COURIER, data = courier[1])
        with allure.step('Получаем id созданного курьера'):
            id_login = response_login.json()['id']
        with allure.step('Создаем Url для удаления курьера'):
            url_for_delete = f'{Urls.URL_DELETE_COURIER}{id_login}'
        with allure.step('Удаляем курьера'):
            response_delete = requests.delete(url_for_delete)
        with allure.step('Проевяем код ответа'):
            assert response_delete.status_code == 200, \
            f'Ожидаемый код ответа: 200, Фактический код ответа: {response_delete.status_code}'
        with allure.step('Проверяем сообщение ответа'):
            assert response_delete.json() == RequestsAnswer.answer_delete_exist_courier, \
            f'Ожидаемое сообзение ответа: {RequestsAnswer.answer_delete_exist_courier}, Фактическое сообщение ответа: {response_delete.json()}'
        with allure.step('Попытка залогинится повторна с удаленным курьером'):
            response_login_after_delete = requests.post(Urls.URL_LOGIN_COURIER, data = courier[1])
        with allure.step('Проверка кода ошибки'):
            assert response_login_after_delete.status_code == 404, \
            f'Ошибаемый код ошибки: 404, Актический код ошибки: {response_login_after_delete}'

    @allure.title('Проверка удаления курьера без id')
    @allure.description('Проверяем возможнсоть удаления курьера без id')
    def test_delete_without_id(self):
        with allure.step('Отправляем запрос на удаление курьера без id'):
            response = requests.delete(Urls.URL_DELETE_COURIER)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 400, \
            f'Ожидаемый код ответа: {400}, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем сообщение об ошибке'):
            assert response.json()['message'] == RequestsAnswer.answer_delete_without_id, \
            f'Ожидаемый ответ: {RequestsAnswer.answer_delete_without_id}, Фактический ответ: {response.json()['message']}'

    @allure.title('Проверка удаления несуществующего курьера')
    @allure.description('Проверяем вохможность удаления несуществующего курьера')    
    def test_delete_nonexist_courier(self):
        with allure.step('Создаем url для удаления несуществующего курьера'):
            url_for_delete = f'{Urls.URL_DELETE_COURIER}987654321'
        with allure.step('Удаляем несуществующего курьера'):
            response = requests.delete(url_for_delete)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 404, \
            f'Ожидаемый код ответа: 404, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем сообщение об ошибке'):
            assert response.json()['message'] == RequestsAnswer.answer_delete_nonexist_courier, \
            f'Ожидаемое сообщение об ошибке: {RequestsAnswer.answer_delete_nonexist_courier}, Фактическое сообщение об ошибке: {response.json()['message']}'
