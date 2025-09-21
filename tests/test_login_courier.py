import requests
import allure
from urls import Urls
from data import RequestsAnswer, Courier



class TestLoginCourier():

    @allure.title('Проверка логина курьера свалидными данными')
    @allure.description('Создаем курьера и пытаемся залогиниться')
    def test_login_with_all_valid_params(self, create_courier_for_login):
        with allure.step('Отправляем запрос на оогин курьера с валидными параметрами'):
            response = requests.post(Urls.URL_LOGIN_COURIER, create_courier_for_login[1])
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 200, \
            f'Ожидаемый код ответа: 200, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем наличие id в ответе, и id типа int'):
            assert 'id' in response.json(), \
            f'Ответ: {response.json()}'
            assert isinstance(response.json().get('id'), int)

    @allure.title('Проверка логина курьера без логина')
    @allure.description('Создаем курьера, регигистрируем его, пытаемся залогинится без логина и с валидным паролем')
    def test_login_without_login(self, create_courier_for_login):
        with allure.step('Создаем курьера для логина без логина и с валидным паролем'):
            payload = {'login': '', 'password' : create_courier_for_login[3]}
        with allure.step("Отправялем запрос на логин курьера без логина"):
            response = requests.post(Urls.URL_LOGIN_COURIER, data = payload)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 400, \
            f'Ожидаемый код овета: 400, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем сообщение об ошибке'):
            assert response.json() == RequestsAnswer.answer_login_invalid, \
            f'Ожидаемое сообщение: {RequestsAnswer.answer_login_invalid}, Фактическое сообщение: {response.json()}'

    @allure.title('Проверка логина курьера без пароля')
    @allure.description('Создаем и регистрируем курьера, пытаемся залогинится с валидным логином и без пароля')
    def test_login_without_password(self, create_courier_for_login):
        with allure.step("Создаем курьера с валидным логином и без пароля"):
            payload = {'login': create_courier_for_login[2], 'password' : ''}
        with allure.step('Отправляем запрос на логин курьера без пароля'):
            response = requests.post(Urls.URL_LOGIN_COURIER, data = payload)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 400, \
            f'Ожидаемый код овета: 400, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем сообщение об ошибке'):
            assert response.json() == RequestsAnswer.answer_login_invalid, \
            f'Ожидаемое сообщение: {RequestsAnswer.answer_login_invalid}, Фактическое сообщение: {response.json()}'

    @allure.title('Проыерка логина курьера без логина и пароля')
    @allure.description('Проверяем невозможность залогиниться без логина и пароля')
    def test_login_without_login_password(self):
        with allure.step('Создаем список для отправки запроса для логина без логина и пароля'):
            payload = {'login': '', 'password' : ''}
        with allure.step('Отправляем запрос на логин курьера без логина и пароля'):
            response = requests.post(Urls.URL_LOGIN_COURIER, data = payload)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 400, \
            f'Ожидаемый код овета: 400, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем сообщение об ошибке'):
            assert response.json() == RequestsAnswer.answer_login_invalid, \
             f'Ожидаемое сообщение: {RequestsAnswer.answer_login_invalid}, Фактическое сообщение: {response.json()}'

    @allure.title('Проверка логина с несуществующим логином и паролем')
    @allure.step("Проверяем, что невозможно залогинитсья с несуществующим логином и паролем")
    def test_login_with_invalid_login_password(self):
        with allure.step('Отправляем Запрос на логин курьера с несуществующим логином и паролем'):
            response = requests.post(Urls.URL_LOGIN_COURIER, Courier.invalid_courier_fo_login)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 404, \
            f'Ожидаемый код овета: 404, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем сообщение об ошибке'):
            assert response.json()['message'] == RequestsAnswer.answer_login_invalid_courier, \
            f'Ожидаемоке сообщение: {RequestsAnswer.answer_login_invalid_courier}, Фактическое сообщение об ошибке: {response.json()['message']}'