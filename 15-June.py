import random as ran

# x = int(input("Enter 1st number x : "))
# y = int(input("Enter 1nd number y : "))
# if x > y:
#     print("x is greater")
# else:
#     print("y is greater")

# n = int(input("Enter the number : "))
# if n%2 == 0:
#     n += 4
# else:
#     n += 7
# print(f"The number is now :{n}")

# sec = ran.randint(1,10)  
# x = int(input("Enter your guess number (1-10) : "))
# if x == sec:
#     print("Correct Answer")
# elif x > sec :
#     print(f"Your guess was High!!\nThe number was {sec}")
# else:
#     print(f"Your guess was Low!!\nThe number was {sec}")

# num = int(input("Enter your number : "))
# if num >= 0 :
#     if num == 0:
#         print("Number is Zero 0")
#     else:
#         print("Number is Positive")
#         if num%2 == 0 :
#             print("Number is Even")
#         else:
#             print("Number is Odd")
# else:
#     print("Number is Negative")

# a = int(input("Enter 1st number : "))
# b = int(input("Enter 2nd number : "))
# c = int(input("Enter 3rd number : "))
# if(a>b):
#     if (a>c):
#         print("A is max")
#     else:
#         print("C is max")
# else:
#     if (b>c):
#         print("B is max")
#     else:
#         print("C is max")

# ex = int(input("Enter your Exam Score (1-100) : "))
# if 90 <= ex <= 100 :
#     print("Grade is A")
# elif 80 <= ex <= 89 :
#     print("Grade is B")
# elif 70 <= ex <= 79 :
#     print("Grade is C")
# elif 60 <= ex <= 69 :
#     print("Grade is D")
# else:
#     print("Grade is F")

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end='')
#     print()

# i = 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(i*j,end=' ')
#         j += 1
#     print()
#     i += 1

# l = [1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     print(i*i,end=' ')

# sum = 0
# sum_1 = 0
# n = 0
# i = 0
# while i <=50 :
#     n += i
#     if i%2 != 0:
#        sum += i
#     else:
#         sum_1 += i
#     i+=1  
# print(sum)
# print(sum_1)
# print(n)

# sum = 0
# i = 1
# while i <=50 :
#     if i%2 != 0:
#        sum += i
#     i+=1  
# print(sum)

# for i in range(1,51):
#     if i%7 == 0:
#         continue
#     print(i)

# i = 0
# while i <= 50:
#     if i%7 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

# n = input("Enter your sequence seperated by commas : ").split(',')
# sum = 0
# for i in n:
#     try:
#         num = int(i)
#         sum += num
#     except ValueError:
#         print("Invalid input")
# print(sum)

# seq = input("Enter your sequence with commas : ").split(',')
# sum = 0
# for i in seq:
#     try:
#         n = int(i.strip())
#         if n%2 == 0:
#             sum += n
#     except ValueError:
#         print("Invalid input")
#         print(n)
#         break
# print(f"Sum is {sum}")

# i = 0
# count = 0
# while i == 0:
#     x = ran.randint(1,10)
#     count += 1
#     print(x)
#     if x > 7:
#         break
# print(f"{count} numbers were generated till greater number than 7 =>> {x} was generated")

# d = {'a':10,'b':20,'c':30,'d':40}
# print(d.keys())
# print(d.values())
# print(d.items())

# def fact(n):
#     if n == 1:
#         return n
#     else:
#         return n*fact(n-1)
# print("Factorial of 5 is :",fact(5))

# def cel_to_far(cel):
#     return [cel*9/5+32]
# cel = float(input("Enter the celsius temperature : "))
# print(f"{cel} Celsius = {cel_to_far(cel)} Farenheit")

# l = [1,2,3,4,5]
# mul = 1
# for i in l:
#     mul *= i
# print(mul)

# a = input("Enter text to Detect : ").lower()
# if a == a[::-1]:
#     print("Yes, Palindrome!!")
# else:
#     print("No, Palindrome!!")

# def is_palindrome(text):
#     if len(text) <= 1:
#         return True
#     if text[0] != text[-1]:
#         return False
#     return is_palindrome(text[1:-1])
# s = input("Enter a string: ").lower()
# if is_palindrome(s):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# a,b = 0,1
# for i in range(10):
#     print(a,end=' ')
#     a,b = b,a+b