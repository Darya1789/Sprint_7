import pytest
import requests
import allure
from urls import Urls
from data import RequestsAnswer
from helper import GenerateInvalidCourier

class TestCreateCourier():
    
    @allure.title('Проверка создания курьера с валидными данными')
    @allure.description('Создаем курьера с валидными логином, паролем и именем, проверяем, что курьер создан, через код ответа и сообщение в ответе')
    def test_create_courier_with_all_params(self, create_courier_for_registration):
        with allure.step('Создаем курьера'):
            response = requests.post(Urls.URL_CREATE_COURIER, create_courier_for_registration[0])
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 201, \
            f'Ожидаемый код ответа: 201, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем сообщение об успешном создании курьера'):
            assert response.json() == RequestsAnswer.answer_create_courier_done, \
            f'Ожидаемое сообщение: {RequestsAnswer.answer_create_courier_done}, Фактическое сообщение: {response.json()}'

    @allure.title('Проверка невозможности создания курьера с логином, который уже есть')
    @allure.description('Создаем курьера с помощью генератора логина и пароля. Пытаемся создать еще одного курьера с таким же логином и паролем')
    def test_create_two_same_courier(self, create_courier_for_registration):
        with allure.step('Создаем курьера с логином и поролем полученным с помощью генерации'):
            requests.post(Urls.URL_CREATE_COURIER, create_courier_for_registration[0])
        with allure.step("Пытаемя создать курьера который уже существует"):
            response_sesond = requests.post(Urls.URL_CREATE_COURIER, create_courier_for_registration[0])
        with allure.step('Проверяем код ответа'):
            assert response_sesond.status_code == 409, \
            f'Ожидаемый код: {409}, Фактический код: {response_sesond.status_code}'
        with allure.step('Проверяем сообщение об ошибке'):
            assert response_sesond.json() == RequestsAnswer.answer_create_two_same_courier, \
            f'Ожидаемое сообение об ошибке: {RequestsAnswer.answer_create_two_same_courier}, Фактическое сообщение об ошибке: {response_sesond.json()}'


    @allure.title('Проверка создания курьера без обязательных параметров')
    @allure.description('Проверяем, что невозможность создать курьера без логина, без пароля, без логина и пароля')
    @pytest.mark.parametrize('courier', [
        GenerateInvalidCourier.generate_create_courier_without_login(), 
        GenerateInvalidCourier.generate_create_courier_without_password(),
        GenerateInvalidCourier.generate_create_courier_without_login_password()])
    def test_create_courier_without_required_params(self, courier):
        with allure.step('Создаем курьера без обязательного параметра'):
            response = requests.post(Urls.URL_CREATE_COURIER, data = courier)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 400, \
            f'Ожидаемый код ответа: 400, Фактический код ответа: {response.status_code}'
        with allure.step('Проверяем сообщение об ошибке'):
            assert response.json() == RequestsAnswer.answer_create_courier_invalid, \
            f'Ожидаемое сообщение об ошибке: {RequestsAnswer.answer_create_courier_invalid}, Фактическиое сообщение об ошибке: {response.json()}'