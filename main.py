#Методи - функції які дозволяють виконувати певні дії

# class Student:
#     def __init__(self, height=160): #функція для ініціалізації параметрів(властивостей)
#         self.height=height
#
#     def __str__(self):
#         return f"I'm a Student. My height is {self.height}"
#
#     def __del__(self):
#         print("End!")\
#
#     def __bool__(self):
#         return self.height !=None
#
#     def __len__(self):
#         return self.height
#
#     def grow(self,cm=1):
#         self.height+=cm
#
#
# nick=Student()
# nick.grow(cm=15)
# print(nick.height)
# print(nick)


# class Auto:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def change_parameter(self, parameter, value):
#         if hasattr(self, parameter):
#             setattr(self, parameter, value)
#             print(f"Параметр '{parameter}' змінено на '{value}'.")
#         else:
#             print(f"Параметр '{parameter}' не існує!")
#
#     def __str__(self):
#         return f"Марка: {self.brand}, Модель: {self.model}, Рік: {self.year}"
#
#
# # Приклад використання
# auto1 = Auto("BMW", "X5", 2021)
# print(auto1)  # автоматично викликає __str__
#
# auto1.change_parameter("year", 2024)
# auto1.change_parameter("brand", "Audi")
#
# print(auto1)


#2
# from datetime import datetime
#
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title      # назва книги
#         self.author = author    # автор книги
#         self.year = year        # рік видання книги
#
#     def get_age(self):
#         current_year = datetime.now().year
#         return current_year - self.year  # повертаємо вік книги
#
#     def __str__(self):
#         return f"Назва: '{self.title}', Автор: {self.author}, Рік видання: {self.year}, Вік книги: {self.get_age()} років"
#
#
# # --- приклад використання ---
# book1 = Book("Кобзар", "Тарас Шевченко", 1840)
# book2 = Book("Гаррі Поттер і філософський камінь", "Дж. К. Ролінґ", 1997)
#
# print(book1)
# print(book2)

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         pi = 3.14159
#         return pi * (self.radius ** 2)
#
#     def __str__(self):
#         return f"Коло з радіусом {self.radius}, площа = {self.calculate_area():.2f}"
#
#
# circle1 = Circle(5)
# print(circle1)

#Зв'язок класів - це взаємодія декількох класів одночасно

# class Human:
#     def __init__(self,name="Human"):
#         self.name=name
#
# class Avto:
#     def __init__(self,brand):
#         self.brand=brand
#         self.passengers = []
#     def AddPassengers(self,human):
#         self.passengers.append(human)
#     def NamePassengers(self):
#         if self.passengers!=[]:
#             print(f"Names of {self.brand} passengers: ")
#             for passenger in self.passengers:
#                 print(passenger.name)
#         else:
#             print(f"There are no passengers in {self.brand}")
#
# nick=Human("Nick")
# kate=Human("Kate")
# car=Avto("Audi")
# car.AddPassengers(nick)
# car.AddPassengers(kate)
# car.NamePassengers()

# 1. Створити клас Student з параметрами ім’я та вік.
# 2. Створити клас ГрупаC2211, де можна додавати студентів і виводити їх усіх.
# 3. Зробити зв’язок між класами.

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"Студент: {self.name}, Вік: {self.age}"
#
#
# class GroupC2211:
#     def __init__(self):
#         self.students = []
#
#     def addstudent(self, student):
#
#         self.students.append(student)
#         print(f"Додано: {student.name}")
#
#     def show_students(self):
#         print("\nСписок студентів групи C2211:")
#         for s in self.students:
#             print(s)
#
#
# student1 = Student("Матвій", 12)
# student2 = Student("Костя", 13)
# student3 = Student("Артем", 13)
#
# group = GroupC2211()
# group.addstudent(student1)
# group.addstudent(student2)
# group.addstudent(student3)
#
# group.show_students()

# Успадкування класів Методи Super.
#Успадкування передача властивостей з батьківського класу в дочірній класам
#Human -> Student Human -> worker
# class Human:
#     height = 170
#     age = 18
#
# class Student(Human):
#     age = 13
#
# class Worker(Human):
#     age = 23
#
# student=Student()
# worker=Worker()
# print(student.height)
# print(worker.height)

# class Grandparent:
#     height = 170
#     name = "Jack"
#     age = 60
#
# class Parent(Grandparent):
#     age = 40
#
# # class Child(Parent):
# #     height = 50
# #     def __init__(self):
# #         print(self.height)
# #         print(self.name)
# #         print(self.age)
# #     def __str__(self):
# #         return f"{self.height}{self.name}{self.age}"
# #
# # nick = Child()
# # print(nick)
# class Class1:
#     var = 20
#     def __init__(self):
#         self.var = 10
#
# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#
#
#
# hello_world = Class2()