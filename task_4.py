# Задание 4
# Напиши класс EmployeeSalary. Он рассчитывает почасовую заработную плату сотрудников за неделю.
# 1. С помощью переменной hourly_payment установи почасовой уровень оплаты, равный 400.
# 2. Проинициализируй атрибуты name, hours, rest_days, email через конструктор.
# 3. Добавь метод класса get_hours(). Если значение hours неизвестно, метод рассчитывает часы, 
# исходя из количества выходных — rest_days. Формула для этого случая такая: (7 - rest_days) * 8.
# 5. Добавь метод класса get_email(). Если значение email неизвестно, метод генерирует его так: 
# f"{name}@email.com".
# 6. Добавь метод класса set_hourly_payment(). Он меняет значение переменной hourly_payment.
# 7. Добавь метод расчёта заработной платы salary(). Формула расчёта такая: hours * hourly_payment.

class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f'{str.lower(name)}@email.com'
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment

# Создание объектов через разные методы
emp1 = EmployeeSalary.get_hours(
    name="Alisa", 
    rest_days=3, 
    email="alisa@example.com"
)
emp2 = EmployeeSalary.get_email(
    name="Marusya", 
    hours=25, 
    rest_days=3
)

print(f'Часы {emp1.name}: {emp1.hours}')
print(f'Почта {emp2.name}: {emp2.email}')

print("Расчёт зарплаты:")
print(emp1.name, emp1.salary())
print(emp2.name, emp2.salary())

print("Изменение почасовой ставки:")
EmployeeSalary.set_hourly_payment(450)
print(emp1.name, emp1.salary())
print(emp2.name, emp2.salary())