import random
import string

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
class GenerateNewCourier():

    @staticmethod
    def register_new_courier_and_return_login_password():
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string


        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload_registration = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        payload_login = {
            "login": login,
            "password": password,
        }

        # возвращаем список
        return payload_registration, payload_login, login, password, first_name
    

class GenerateInvalidCourier:

    @staticmethod
    def generate_create_courier_without_login():
        courier = {
            '', 
            GenerateNewCourier.register_new_courier_and_return_login_password()[3],
            GenerateNewCourier.register_new_courier_and_return_login_password()[4]
            }
        return courier
    
   
    @staticmethod
    def generate_create_courier_without_password():
        courier = {
            GenerateNewCourier.register_new_courier_and_return_login_password()[2], 
            '',
            GenerateNewCourier.register_new_courier_and_return_login_password()[4]
            }
        return courier
    
    @staticmethod
    def generate_create_courier_without_login_password():
        courier = {
            '', 
            '',
            GenerateNewCourier.register_new_courier_and_return_login_password()[4]
            }
        return courier
    

    @staticmethod
    def generate_login_courier_without_login():
        courier = {
            '', 
            GenerateNewCourier.register_new_courier_and_return_login_password()[3]
            }
        return courier
    
   
    @staticmethod
    def generate_login_courier_without_password():
        courier = {
            GenerateNewCourier.register_new_courier_and_return_login_password()[2], 
            ''
            }
        return courier
    
    @staticmethod
    def generate_login_courier_without_login_password():
        courier = {
            '', 
            ''
            }
        return courier