# class Dog:
#     species = "Canine"

#     def Dialogue(self):
#         print("Sari duniya humse BHAU BHAU bole se!!!!")

#     def bark(self):
#         print("Woof!")

# Dogesh_Bhai = Dog()
# Dogesh_Bhai.bark()
# Dogesh_Bhai.Dialogue()

# class Dog:
#     species = "Canine"

#     def bark(self):
#         print("Woof!")

# rex = Dog()
# rex.name = "Rex"
# rex.age = 5
# print(rex.name)
# print(rex.age)
# rex.bark()

# # Library_Book_Class

# class Book:
#     def __init__(self, title, author, is_borrowed = False):
#         self.title = title
#         self.author = author
#         self.is_borrowed = is_borrowed

#     def display_info(self):
#         print(f"Title: {self.title}\nAuthor: {self.author}\nBorrowed: {self.is_borrowed}\n")

# Book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", True)
# Book1.display_info()

# Book2 = Book("To Kill a Mockingbird", "Harper Lee")
# Book2.display_info()

# Book3 = Book("1984", "George Orwell", True)
# Book3.display_info()

# # Bank Account Class

# class BankAccount:
#     def __init__(self, balance = 0):
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited: ${amount}\n")
#         else:
#             print("Deposit amount must be positive.\n")

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew: ${amount}\n")
#         else:
#             print("Invalid withdrawal amount.\n")
    
#     def display_balance(self):
#         print(f"Current Balance: ${self.balance}\n")
    
# account = BankAccount(100)
# account.display_balance()
# account.deposit(50)
# account.display_balance()
# account.withdraw(30)
# account.display_balance()

# # Reactangle Class

# class Rectangle:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width

#     def area(self):
#         return self.height * self.width

#     def perimeter(self):
#         return 2 * (self.height + self.width)
    
# rect1 = Rectangle(5, 3)
# print(f"Length: {rect1.height} Width: {rect1.width}")
# print(f"Area: {rect1.area()}")
# print(f"Perimeter: {rect1.perimeter()}")
# rect2 = Rectangle(10, 4)
# print(f"Length: {rect2.height} Width: {rect2.width}")
# print(f"Area: {rect2.area()}")
# print(f"Perimeter: {rect2.perimeter()}")
# rect3 = Rectangle(7, 2)
# print(f"Length: {rect3.height} Width: {rect3.width}")
# print(f"Area: {rect3.area()}")
# print(f"Perimeter: {rect3.perimeter()}")