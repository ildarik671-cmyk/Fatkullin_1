# **Задача 1**
# Создай родительский класс `Animal`, у которого есть метод `speak()`.
# Этот метод должен выводить на экран фразу "Я - животное".
# Затем создай дочерний класс `Dog`, который наследует от `Animal`.
# Переопредели в классе `Dog` метод `speak()` так, чтобы он выводил на экран фразу "Гав!".
# Создай экземпляр класса `Dog` и вызови у него метод `speak()`.

class Animal:
    def speak(self):
        print("Я - животное")
class Dog(Animal):
    def speak(self):
        print("Гав")

# Теперь давай проверим, как это работает, и добавим вызов.
# Ты создал классы, но программа пока ничего не делает.
# Чтобы увидеть результат, нужно создать объект (экземпляр) класса Dog и вызвать у него метод speak().
# Добавь в конец кода создание объекта и вызов метода.

class Animal:
    def speak(self):
        print("Я - животное")
class Dog (Animal):
    def speak(self):
        print("Гав")
dog1 = Dog()
dog1.speak()


# **Задача 3**
# Создай класс `Device` (Устройство).
# *   В `__init__` сохраняй атрибуты: `brand` (бренд) и `model` (модель).
# *   Создай метод `get_info`, который возвращает строку (не печатает, а именно возвращает через `return`) вида: `"Бренд: {brand}, Модель: {model}"`.
# Создай класс `Smartphone` (Смартфон), который наследует `Device`.
# *   В `__init__` класса `Smartphone` добавь новый атрибут `os` (операционная система).
# *   Используй вызов родительского конструктора через `Device.__init__(self, brand, model)` для установки бренда и модели.
# *   Переопредели метод `get_info` так, чтобы он возвращал строку: `"Смартфон: Бренд: {brand}, Модель: {model}, ОС: {os}"`.
# Создай объект `my_phone` класса `Smartphone` с любыми параметрами и выведи результат работы его метода `get_info()` на экран (используй `print`).

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def get_info(self):
        return f"Бренд: {self.brand}, Модель: {self.model}"
class Smartphone(Device):
    def __init__(self, brand, model, os):
        Device.__init__(self, brand, model)
        self.os = os
    def get_info(self):
        return f"Смартфон: Бренд: {self.brand}, Модель: {self.model}, ОС: {self.os}"
# Остался последний шаг — проверить, как это работает. Добавь в конец кода создание объекта и вывод результата.
my_phone = Smartphone("Realme", "C55", "Android")
print(my_phone.get_info())


# **Задача 4**
# Создай класс `Employee` (Сотрудник).
# *   В `__init__` сохраняй `name` (имя) и `salary` (зарплата).
# *   Создай метод `show_info`, который печатает: `"Сотрудник: {name}, Зарплата: {salary}"`.
# Создай класс `Manager` (Менеджер), который наследует `Employee`.
# *   В `__init__` добавь новый атрибут `team_size` (размер команды).
# *   Используй вызов родительского конструктора через `Employee.__init__(self, name, salary)`.
# *   Переопредели метод `show_info` так, чтобы он печатал: `"Менеджер: {name}, Зарплата: {salary}, Команда: {team_size} человек"`.
# Создай одного менеджера и вызови для него метод `show_info()`.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show_info(self):
        print(f"Сотрудник: {self.name}, Зарплата: {self.salary}")
class Manager(Employee):
    def __init__(self,name, salary, team_size):
        Employee.__init__(self, name, salary)
        self.team_size = team_size
    def show_info(self):
        print(f"Менеджер: {self.name}, Зарплата: {self.salary}, Команда: {self.team_size} человек")
employeeName = Manager("Ильдар",100000,15)


# **Задача 5**
# Создай класс `Product` (Товар).
# *   В `__init__` сохраняй `name` (название) и `price` (цена).
# *   Создай метод `get_price`, который возвращает цену товара.
# Создай класс `DiscountedProduct` (Товар со скидкой), который наследует `Product`.
# *   В `__init__` добавь новый атрибут `discount` (скидка в процентах, например 10 для 10%).
# *   Используй вызов родительского конструктора через `Product.__init__(self, name, price)`.
# *   **Переопредели** метод `get_price` так, чтобы он возвращал цену с учетом скидки. Формула: `price * (100 - discount) / 100`.
# Создай объект `DiscountedProduct` с названием "Футболка", ценой 1000 и скидкой 20.
# Выведи на экран результат вызова метода `get_price()` у этого объекта (через `print`).

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_price(self):
        return self.price
class DiscountedProduct(Product):
    def __init__(self,discount, name, price):
        Product.__init__(self, name, price)
        self.discount = discount
    def get_price(self):
        return self.price * (100 - self.discount) / 100
total_price = DiscountedProduct(20, "Футболка", 1000)
print(total_price.get_price())


# **Задача 6**
# Создай класс `BankAccount` (Банковский счет).
# *   В `__init__` сохраняй `owner` (владелец) и `balance` (баланс, по умолчанию 0).
# *   Создай метод `deposit(self, amount)`, который добавляет сумму к балансу и печатает: `"Пополнено: {amount}. Баланс: {balance}"`.
# *   Создай метод `withdraw(self, amount)`, который вычитает сумму из баланса и печатает: `"Снято: {amount}. Баланс: {balance}"`.
# Если денег недостаточно, печатай: `"Недостаточно средств"`.
# Создай класс `SavingsAccount` (Сберегательный счет), который наследует `BankAccount`.
# *   В `__init__` добавь новый атрибут `interest_rate` (процентная ставка).
# *   Используй вызов родительского конструктора через `BankAccount.__init__(self, owner, balance)`.
# *   Создай новый метод `apply_interest()`, который увеличивает баланс на процент (`balance += balance * interest_rate / 100`)
# и печатает: `"Начислены проценты. Баланс: {balance}"`.
# Создай объект `SavingsAccount` с владельцем "Анна", начальным балансом 1000 и ставкой 5%.
# Вызови метод `deposit(500)`, затем метод `apply_interest()`, затем метод `withdraw(200)`.

class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Пополнено: {amount}. Баланс: {self.balance}")
    def withdraw(self, amount):
        if self.balance  >= amount :
            self.balance -= amount
            print(f"Снято: {amount}. Баланс: {self.balance}")
        else:
            print("Недостаточно средств")
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        BankAccount.__init__(self, owner, balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate / 100
        print(f"Начислены проценты. Баланс: {self.balance}")
result = SavingsAccount("Анна",1000, 5)
result.deposit(500)
result.apply_interest()
result.withdraw(2000)


# **Задача 7**
# Создай класс `Book` (Книга).
# *   В `__init__` сохраняй `title` (название) и `author` (автор).
# *   Создай метод `get_info`, который возвращает строку: `"Книга: {title}, Автор: {author}"`.
# Создай класс `LibraryBook` (Библиотечная книга), который наследует `Book`.
# *   В `__init__` добавь новый атрибут `is_borrowed` (статус: взята или нет). По умолчанию `False` (не взята).
# *   Используй вызов родительского конструктора через `Book.__init__(self, title, author)`.
# *   Создай метод `borrow()`, который:
#     *   Если книга не взята (`is_borrowed == False`), меняет статус на `True` и печатает: `"Книга выдана"`.
#     *   Если книга уже взята, печатает: `"Книга уже выдана"`.
# *   Создай метод `return_book()`, который:
#     *   Если книга взята (`is_borrowed == True`), меняет статус на `False` и печатает: `"Книга возвращена"`.
#     *   Если книга не была взята, печатает: `"Книга не была выдана"`.
# *   Переопредели метод `get_info` так, чтобы он возвращал строку: `"Книга: {title}, Автор: {author}, Статус: {взята/доступна}"`.
# Статус "взята", если `is_borrowed == True`, и "доступна", если `False`.
# Создай объект `LibraryBook` с названием "Война и мир" и автором "Толстой".
# Вызови метод `borrow()`, затем метод `get_info()` и выведи результат на экран (через `print`).

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def get_info(self):
        return f"Книга: {self.title}, Автор: {self.author}"
class LibraryBook(Book):
    def __init__(self, title, author,is_borrowed = False):
        Book.__init__(self, title, author)
        self.is_borrowed = is_borrowed
    def borrow(self):
            if not self.is_borrowed:
                self.is_borrowed = True
                print("Книга выдана")
            else:
                print("Книга уже выдана")
    def return_book(self):
        if  self.is_borrowed:
            self.is_borrowed = False
            print("Книга возвращена")
        else:
            print("Книга не была выдана")
    def get_info(self) :
        status = "взята" if self.is_borrowed else "доступна"
        return f"Книга: {self.title}, Автор: {self.author}, Статус: {status}"
result = LibraryBook("Война и мир", "Толстой")
result.borrow()
print(result.get_info())










