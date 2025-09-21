import re
from tkinter import Y
import requests
import pytest
import json
from data import Order
from helper import GenerateNewCourier
from urls import Urls


@pytest.fixture()
def create_courier_for_registration():
    data =  GenerateNewCourier.register_new_courier_and_return_login_password()
    yield data
    login = requests.post(Urls.URL_LOGIN_COURIER, data = data[1])
    requests.delete(f'{Urls.URL_DELETE_COURIER}{login.json()["id"]}')

@pytest.fixture()
def create_courier_for_login(create_courier_for_registration):
    requests.post(Urls.URL_CREATE_COURIER, data = create_courier_for_registration[0])
    return create_courier_for_registration

@pytest.fixture()
def login_courier_and_return_id(create_courier_for_login):
    response = requests.post(Urls.URL_LOGIN_COURIER, data = create_courier_for_login[1])
    return response.json()['id']

@pytest.fixture()
def create_order_and_return_id():
    order = Order.order_data
    order['color'] = ['Black']
    order = json.dumps(order)
    response = requests.post(Urls.URL_CREATE_ORDER, data = order)
    yield response.json()['track']
    requests.put(Urls.URL_CANCEL_ORDER, params={'track': response.json()['track']})



