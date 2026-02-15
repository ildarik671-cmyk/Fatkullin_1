# **Задача 1**
# Создай класс `Book`.
# У класса должен быть **общий атрибут** `material` со значением `"бумага"`.
# Создай два экземпляра этого класса (объекта).
# Выведи на экран значение атрибута `material` для любого из созданных объектов.

class Book:
    material = "бумага"
    def __init__(self, name, author):
        self.name = name
        self.author = author
material1 = Book(name="Ильдар",author="Warhammer")
print(material1.material)


# **Задача 2**
# # Создай класс `Car`.
# # У класса должен быть **конструктор**, который принимает три параметра:
# # `brand` (марка), `model` (модель), `year` (год выпуска).
# # Все эти параметры нужно сохранить как атрибуты экземпляра.
# # Создай один объект этого класса и выведи на экран марку и год выпуска этого автомобиля (каждый атрибут выведи отдельным вызовом `print`).

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
car = Car(brand = "Toyota",model = "Corolla", year = 2019)
print(car.brand)
print(car.year)


# **Задача 3**
# Создай класс `Student`.
# У класса должен быть **конструктор**, который принимает один параметр:
# `name` (имя студента) и сохраняет его как атрибут экземпляра.
# Также у класса должен быть **метод** `say_hello`, который выводит на экран фразу:
# `"Привет, меня зовут <имя>"`, где `<имя>` — это имя студента.
# Создай один объект класса и вызови у него метод `say_hello`.

class Student:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(f"Привет, меня зовут {self.name}")
nameStud =  Student("Ильдар")
nameStud.say_hello()


# **Задача 4**
# Создай класс `Cat`.
# У класса должен быть **конструктор**, который принимает два параметра:
# `name` (имя кота) и `age` (возраст).
# Оба параметра нужно сохранить как атрибуты экземпляра.
# Также у класса должен быть **метод** `meow`, который выводит на экран фразу:
# `"<имя> говорит: Мяу!"`, где `<имя>` — имя кота.
# Создай один объект класса с любым именем и возрастом, затем вызови у него метод `meow`.

class Cat:
    def __init__(self,name, age ):
        self.name = name
        self.age = age
    def meow(self):
        print(f"{self.name} {self.age} лет говорит: Мяу!")
catKatya = Cat(name = "Katucha" , age = 18 )
catKatya.meow()


# **Задача 5**
# Создай класс `Counter`.
# У класса должен быть **конструктор**, который принимает один параметр:
# `start_value` (начальное значение счётчика) и сохраняет его как атрибут экземпляра.
# Также у класса должен быть **метод** `increment`, который **увеличивает значение счётчика на 1** (изменяет атрибут).
# Создай один объект класса со стартовым значением 5.
# Вызови метод `increment` один раз, затем выведи текущее значение счётчика на экран.


class Counter:
    def __init__(self, start_value):
        self.start_value = start_value
    def increment(self):
        self.start_value += 1
        print(self.start_value)
num = Counter(999)
num.increment()


# **Задача 6**
# Создай класс `Phone`.
# У класса должен быть **общий атрибут** `country` со значением `"Китай"`.
# Также у класса должен быть **конструктор**, который принимает один параметр:
# `model` (модель телефона) и сохраняет его как атрибут экземпляра.
# Создай два объекта этого класса с разными моделями.
# Выведи на экран страну производителя и модель для каждого телефона (можно в одной строке или разными print — как удобно).

class Phone:
    country = "Китай"
    def __init__(self, model):
        self.model = model
phone1 = Phone("Xiaomi")
phone2 = Phone("Samsung")
print(phone1.country + " " + phone1.model)
print(phone2.country + " " +  phone2.model)

# **Задача 7**
# Создай класс `BankAccount`.
# У класса должен быть **конструктор**, который принимает два параметра:
# `owner` (владелец счёта) и `balance` (баланс).
# Сохрани их как атрибуты экземпляра.
# Также у класса должен быть **метод** `deposit`, который принимает один параметр `amount` (сумма) и **увеличивает баланс** на эту сумму.
# Метод ничего не выводит на экран, только изменяет атрибут.
# Создай один объект класса с владельцем `"Иван"` и балансом `1000`.
# Вызови метод `deposit` с суммой `500`.
# Выведи на экран итоговый баланс.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
result = BankAccount(owner= "Иван", balance=1000 )
result.deposit(500)
print(result.balance)


# **Задача 8**
# Создай класс `Rectangle`.
# У класса должен быть **конструктор**, который принимает два параметра:
# `width` (ширина) и `height` (высота).
# Сохрани их как атрибуты экземпляра.
# Также у класса должен быть **метод** `area`, который **возвращает** (не выводит, а именно возвращает через `return`) площадь прямоугольника.
# Создай один объект класса с шириной 5 и высотой 10.
# Вызови метод `area` у этого объекта и выведи результат на экран.

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
square = Rectangle(5,20)
print(square.area)

# **Задача 9**
# Создай класс `Dog`.
# У класса должен быть **общий атрибут** `species` со значением `"собака"`.
# Также у класса должен быть **конструктор**, который принимает один параметр:
# `name` (имя собаки) и сохраняет его как атрибут экземпляра.
# Кроме этого, у класса должен быть **метод** `bark`, который выводит на экран фразу:
# `"<имя> говорит: Гав!"`.
# Создай два объекта класса с разными именами.
# Для каждого объекта:
# - выведи на экран вид животного (общий атрибут),
# - вызови метод `bark`.

class Dog:
    species = "собака"
    def __init__(self,name):
        self.name = name
    def bark(self):
        print(f"{self.name} говорит: Гав!")
tuzik = Dog("Тузек")
tarzan = Dog("Тарзан")
print(tuzik.species)
print(tarzan.species)
tuzik.bark()
tarzan.bark()


# **Задача 10**
# Создай класс `Employee`.
# У класса должен быть **конструктор**, который принимает три параметра:
# `name` (имя), `position` (должность) и `salary` (зарплата).
# Сохрани их как атрибуты экземпляра.
# Также у класса должен быть **метод** `get_info`, который **возвращает** строку вида:
# `"<имя>, <должность> — зарплата: <зарплата> руб."`
# Создай один объект класса с любыми значениями.
# Выведи результат вызова метода `get_info` на экран.

class Employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary
    def get_info(self):
        return f"{self.name}, {self.position}> — зарплата: {self.salary} руб."
net = Employee("Ильдарыч","тестировщик", 100000)
print(net.get_info())



# **Задача 1**
# Создай класс `Book`.
# У класса должен быть **общий атрибут** `material` со значением `"бумага"`.
# Никаких конструкторов и методов пока не нужно, только класс и общий атрибут.

class Book:
    material = "бумага"



# **Задача 2**
# Создай класс `Car`.
# Добавь **конструктор (`__init__`)** , который принимает параметры `brand` и `year` и сохраняет их как атрибуты объекта.
# Методы пока не нужны.

class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year



# **Задача 3**
# Создай класс `Dog`.
# У класса должен быть **общий атрибут** `species` со значением `"Canis familiaris"`.
# Также добавь **конструктор**, который принимает `name` и `age` и сохраняет их как атрибуты объекта.
# Методы пока не нужны.

class Dog:
    species = "Canis familiaris"
    def __init__ (self,name,age):
        self.name = name
        self.age = age



# **Задача 5**
# Создай класс `BankAccount`.
# Добавь **конструктор**, который принимает `owner` и `balance` (по умолчанию 0).
# Добавь **метод** `deposit(amount)`, который увеличивает баланс на указанную сумму.
# Добавь **метод** `withdraw(amount)`, который уменьшает баланс на указанную сумму (без проверок на отрицательный баланс).

# class BankAccount:
#     def __init__(self, owner, balance = 0):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         self.balance -= amount



# **Задача 6**
# Создай класс `Counter`.
# Добавь **конструктор**, который принимает начальное значение `start` (по умолчанию 0).
# Добавь **общий атрибут** `total_counters` со значением 0 (будет считать количество созданных объектов).
# Каждый раз, когда создаётся новый объект `Counter`, общий атрибут должен увеличиваться на 1.
# Добавь **метод** `increment(self)`, который увеличивает счётчик конкретного объекта на 1.
# Добавь **метод** `value(self)`, который возвращает текущее значение счётчика объекта.

class Counter:
    total_counters = 0
    def __init__(self, start = 0):
        self.start = start
        Counter.total_counters += 1
    def increment(self):
        self.start += 1
    def value(self):
        return self.start



# **Задача 7**
# Создай класс `Rectangle`.
# Добавь **конструктор**, который принимает `width` и `height`.
# Добавь **метод** `area`, который возвращает площадь прямоугольника.
# Добавь **метод** `perimeter`, который возвращает периметр прямоугольника.
# *Без общих атрибутов, только конструктор и методы.*

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width + self.height) * 2










