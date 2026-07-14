# # MRO - Method Resolution Order
# class A:
#     def greet(self): return "Hello class A"

# class B(A):
#     def greet(self): return "Hello class B"

# class C(A):
#     def greet(self): return "Hello class C"

# class D(B,C):          # Multiple Inheritance
#     pass

# d = D()
# print(d.greet())
# print(D.__mro__)
# print([cls.__name__ for cls in D.__mro__])

# # isinstance() & issubclass()
# class Vehicle:
#     pass

# class Car(Vehicle):
#     pass

# class ElectricCar(Car):
#     pass

# tesla = ElectricCar()

# print("isinstance")
# print(f"isinstance(tesla, ElectricCar)   : {isinstance(tesla, ElectricCar)}")
# print(f"isinstance(tesla, Car)           : {isinstance(tesla, Car)}")
# print(f"isinstance(tesla, Vehicle)       : {isinstance(tesla, Vehicle)}")
# print(f"isinstance(tesla, str)           : {isinstance(tesla, str)}")
# print("\nissubclass")
# print(f"issubclass(ElectricCar, Car)     : {issubclass(ElectricCar, Car)}")
# print(f"issubclass(ElectricCar, Vehicle) : {issubclass(ElectricCar, Vehicle)}")
# print(f"issubclass(Car, ElectricCar)     : {issubclass(Car, ElectricCar)}")

# class Person:
#     def __init__(self, name, age):
#         self.name, self.age = name, age

#     def introduce(self):
#         return f"Hi ! I'm {self.name}\nage = {self.age}\n"
    
# class Employee(Person):
#     def __init__(self, name, age, emp_id, dept):
#         super().__init__(name, age)
#         self.emp_id = emp_id
#         self.dept = dept

#     def introduce(self):
#         base = super().introduce()
#         return f"{base}ID = {self.emp_id}\nDept = {self.dept}\n"

# class Manager(Employee):
#     def __init__(self, name, age, emp_id, dept, team_size):
#         super().__init__(name, age, emp_id, dept)
#         self.team_size = team_size

#     def introduce(self):
#         return super().introduce() + f"Team = {self.team_size}\n"
    
# mgr = Manager("Dr. Farooq", 38, "M001", "CSE", 12)
# print(mgr.introduce())

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     def __init__(self, color):
#         self.color = color

#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

#     def describe(self):
#         return f"{self.color} {self.__class__.__name__}\narea = {self.area():.2f}\nperimeter = {self.perimeter():.2f}"

# class Circle(Shape):
#     def __init__(self, r, color = "blue"):
#         super().__init__(color)
#         self.r = r

#     def perimeter(self): return 2 * 3.14159 * self.r    
#     def area(self): return 3.14159 * self.r ** 2

# c = Circle(7)
# print(c.describe())

# # Shape Hierarchy with ABC
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     count = 0

#     def __init__(self, color):
#         self.color = color
#         Shape.count += 1

#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

#     def describe(self):
#         return f"{self.__class__.__name__} ({self.color})\nArea: {self.area():.2f}\nPerimeter: {self.perimeter():.2f}"

#     @classmethod
#     def total_shapes(cls):
#         return cls.count


# class Circle(Shape):
#     def __init__(self, r, color):
#         super().__init__(color)
#         self.r = r

#     def area(self):
#         return 3.14159 * self.r ** 2

#     def perimeter(self):
#         return 2 * 3.14159 * self.r


# class Rectangle(Shape):
#     def __init__(self, length, width, color):
#         super().__init__(color)
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)


# class Triangle(Shape):
#     def __init__(self, a, b, c, color):
#         super().__init__(color)
#         self.a = a
#         self.b = b
#         self.c = c

#     def area(self):
#         s = (self.a + self.b + self.c) / 2
#         return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

#     def perimeter(self):
#         return self.a + self.b + self.c


# def print_report(shapes_list):
#     for shape in shapes_list:
#         print(shape.describe())
#         print("-" * 30)

# shapes = [
#     Circle(5, "Red"),
#     Rectangle(4, 6, "Blue"),
#     Triangle(3, 4, 5, "Green")
# ]

# print_report(shapes)
# print("Total Shapes:", Shape.total_shapes())

# # Vehicle Fleet System
# class Vehicle:
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Vehicle.count += 1

#     def fuel_cost(self, km):
#         return km * 10  


# class Car(Vehicle):
#     def __init__(self, name):
#         super().__init__(name)

#     def fuel_cost(self, km):
#         return km * 8


# class Truck(Vehicle):
#     def __init__(self, name):
#         super().__init__(name)

#     def fuel_cost(self, km):
#         return km * 15


# class Motorcycle(Vehicle):
#     def __init__(self, name):
#         super().__init__(name)

#     def fuel_cost(self, km):
#         return km * 3


# class ElectricCar(Car):
#     def __init__(self, name):
#         super().__init__(name)

#     def fuel_cost(self, km):
#         return 0


# def fleet_report(vehicles, km):
#     for v in vehicles:
#         cost = v.fuel_cost(km)
#         vtype = type(v).__name__
#         print(f"{vtype} ({v.name}) -> Cost for {km} km: {cost}")

#     print("Total vehicles:", Vehicle.count)

# fleet = [
#     Car("Honda"),
#     Truck("Tata"),
#     Motorcycle("Yamaha"),
#     ElectricCar("Tesla")
# ]

# fleet_report(fleet, 100)

# # Multi-Role Staff System
# class Person:
#     def __init__(self, name, **kwargs):
#         super().__init__(**kwargs)
#         self.name = name


# class Employee(Person):
#     def __init__(self, emp_id, **kwargs):
#         super().__init__(**kwargs)
#         self.emp_id = emp_id


# class Teacher(Employee):
#     def __init__(self, subjects, **kwargs):
#         super().__init__(**kwargs)
#         self.subjects = subjects

#     def teach(self):
#         return f"{self.name} teaches {', '.join(self.subjects)}"


# class AdminStaff(Employee):
#     def __init__(self, designation, **kwargs):
#         super().__init__(**kwargs)
#         self.designation = designation

#     def admin_task(self):
#         return f"{self.name} performs {self.designation} tasks"


# class TeacherAdmin(Teacher, AdminStaff):
#     def __init__(self, name, emp_id, subjects, designation):
#         super().__init__(
#             name=name,
#             emp_id=emp_id,
#             subjects=subjects,
#             designation=designation
#         )

#     def show_role(self):
#         return f"{self.teach()}\n{self.admin_task()}"


# print("MRO:", TeacherAdmin.__mro__)

# ta = TeacherAdmin("Nisha", 101, ["Math", "CS"], "Exam Coordinator")
# print(ta.show_role())