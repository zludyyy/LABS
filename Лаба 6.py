class UserAccount:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password: str) -> None:
        self.__password = new_password

    def check_password(self, password: str) -> bool:
        return self.__password == password

class Vehicle:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def get_info(self) -> str:
        return f"Марка: {self.make}, модель: {self.model}"

class Car(Vehicle):
    def __init__(self, make: str, model: str, fuel_type: str):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self) -> str:
        return f"Марка: {self.make}, модель: {self.model}, тип топлива: {self.fuel_type}"

# Задание 1
user = UserAccount("artuir", "arturvol123@gmail.com", "1332231")
print(user.check_password("12345678"))  # True
user.set_password("abcd")
print(user.check_password("12345678"))  # False
print(user.check_password("abcd"))  # True

# Задание 2
vehicle = Vehicle("Toyota", "Mark2")
print(vehicle.get_info())

car = Car("BMW", "M5", "бензин")
print(car.get_info())
