class Car:
    def __init__(self, brand, model, year, top_speed, current_speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self.current_speed = current_speed

    def accelarate(self, amount):
        if self.current_speed + amount <= self.top_speed:
            self.current_speed += amount
            print(f'The {self.brand} accelerates to {self.current_speed} mph')

        else:
            print(f"{self.brand}'s top speed is {self.top_speed}, cannot accelerate to {self.current_speed + amount}")

    def brake(self, amount):
        self.current_speed = max(0, self.current_speed - amount)
        print(f'The {self.brand} slows down to {self.current_speed} mph')


my_car = Car("Toyota", "Corolla", 2020, 120, 0)
my_car.accelarate(50)
my_car.brake(20)
my_other_car = Car("Honda", "Civic", 2022, 120, 0)
my_other_car.accelarate(100)
my_other_car.brake(120)

