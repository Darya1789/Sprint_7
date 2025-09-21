class Courier:
    invalid_courier_fo_login = {'login': 'xxxxxxxxxx', 'password' : 'xxxxxxxxxx'}

class Order:
    order_data = {
        "firstName": "Дарья",
        "lastName": "Дарьина",
        "address": "Ушакова ул., д 25",
        "metroStation": 4,
        "phone": "+79817654321",
        "rentTime": 2,
        "deliveryDate": "2025-10-01",
        "comment": "Жду возле подъезда 1"
    }   


class RequestsAnswer:
    answer_create_courier_done = {'ok': True}
    answer_create_courier_invalid = {'code': 400, "message": "Недостаточно данных для создания учетной записи"}
    answer_create_two_same_courier = {'code': 409, "message": "Этот логин уже используется. Попробуйте другой."}
    answer_login_invalid = {'code' : 400, "message":  "Недостаточно данных для входа"}
    answer_login_invalid_courier = 'Учетная запись не найдена'
    answer_delete_exist_courier = {'ok': True}
    answer_delete_without_id = 'Недостаточно данных для удаления курьера'
    answer_delete_nonexist_courier = 'Курьера с таким id нет.'
    answer_accept_order_valid = {'ok': True}
    answer_accept_order_witout_id_order_id_courier = {'code': 400, 'message': 'Недостаточно данных для поиска'}
    answer_accept_order_with_invalid_id_courier = {'code': 404, 'message': 'Курьера с таким id не существует'}
    answer_accept_order_with_invalid_id_order = {'code': 404, 'message': 'Заказа с таким id не существует'}
    answer_get_order_without_id = {'code': 400, 'message': 'Недостаточно данных для поиска'}
    answer_get_order_with_invalid_id = {'code': 404, 'message': 'Заказ не найден'}
