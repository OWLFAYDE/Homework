import random

class NegativePriceError(Exception):
    pass
class car:
    def __init__(self, brand, color, price, owner):
        if price < 0:
            raise NegativePriceError (f"нельзя создать автомобиль {brand} с отрицвтельным номером")
        self.brand = brand
        self.color = color
        self.price = price
        self.owner = owner

        self._number=random.randint(100,999)
    @property
    def number(self):
        return self._number
    def newColor(self,new_color):
        self.color = new_color
    def newOwner(self,new_owner):
        self.owner = new_owner
    def newBrand(self,new_brand):
        self.brand = new_brand
    def newPrice(self,new_price):
        self.price = new_price
        if new_price <= 0:
            raise NegativePriceError (f"стоимость не может быть отрицательной")
        else :
            self.price = new_price
    def infoCar(self):
        return f"машина - {self.brand} №{self._number} \n Цвет автомобиля - {self.color} \n цена автомобиля {self.price} \n имя владельца - {self.owner}"
try:
    car1 = car("BMW", "white", "120000", "ivan")
    car2 = car("honda", "red", "230000", "igor")
    car3 = car("opel", "blue", "650000", "anna")
    print(car1.infoCar())
    print()
    print(car2.infoCar())
    print()
    print(car3.infoCar())
    print()
except NegativePriceError as e:
    print(f"ошибка {e} ")
try:
    user_brand = input("models for auto: ")
    user_color = input("colors for auto: ")
    user_price = input("price for auto: ")
    user_owner = input("owner of auto: ")

    user_car = car(user_color,user_brand,user_price,user_owner)
    print(f"\nмашина {user_brand} добавлена")
    print(user_car.infoCar())
except ValueError:
    print("\n ошибка, стоимость должна быть числом")
except NegativePriceError as e:
    print(f"ошибка {e}")