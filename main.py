class Vehicle:
    def __init__(self, brand, model, year, color, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
    def get_info(self):
        return f"{self.brand + " " + self.model}\n{self.year} года\nЦвет {self.color}\nЦена {self.price}\n"

    def price_in_a_few_years(self, years):
        devalv = 0.1
        return f"Через {years} год(а)/лет цена будет {self.price * (0.9 ** years)}"

    def update_price(self, new_price):
        self.price = new_price
        return f"Новая цена будет {self.price}"

class Car(Vehicle):
    def __init__(self, brand, model, year, color, price, car_class):
        super().__init__(brand, model, year, color, price)
        self.car_class = car_class
    def is_for_track(self, car_class):
        if self.car_class == "A" or "M" or "J":
            return "Эта машина для трека вряд-ли подойдет"
        if self.car_class == "B":
            return "Супермини будут очень хорошо входить в повороты, так что с натяжкой можно\nиспользовать на треке"
        if self.car_class == "C":
            return "Если машина относ-но легкая, а мотор хороший, то в целом для трека пойдет"
        if self.car_class == "D":
            return "Обычно машины этого класса тяжелые, для трека я бы не рекомендовал"
        if self.car_class == "E" or "F" or "S":
            return "С очень большой вероятностью вы получите много эмоций и ощущений на треке, бегом туда!"

class Truck(Vehicle):
    def __init__(self, brand, model, year, color, price, cargo_capacity):
        super().__init__(brand, model, year, color, price)
        self.cargo_capacity = cargo_capacity

    def load_cargo(self, weight):
        if weight <= self.cargo_capacity:
            return f"Груз успешно загружен. Текущий вес груза: {weight} кг."
        else:
            return f"Груз слишком тяжелый! Максимальная грузоподъемность: {self.cargo_capacity} кг."

    def get_info(self):
        # Расширяем метод get_info, добавляя информацию о грузоподъемности
        base_info = super().get_info()
        return f"{base_info} Грузоподъемность: {self.cargo_capacity} кг."


car = Car("Toyota", "Corolla", 2020, "Красный", 15000, "M")
truck = Truck("Volvo", "FH", 2018, "Синий", 50000, 8000)

# Выводим информацию о транспортных средствах
print(car.get_info())
print(car.is_for_track("S"))
print(car.price_in_a_few_years(5))

print()

print(truck.get_info())
print(truck.load_cargo(7000))
print(truck.price_in_a_few_years(3))