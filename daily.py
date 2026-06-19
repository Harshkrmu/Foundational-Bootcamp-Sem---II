# l = [1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     print(i)

# l1 = [0,1]
# l2 = [0,1]
# for i in l1:
#     for j in l2:
#         print(i,j)

# for i in [10,20]:
#     for j in [1,2]:
#         print(i+j)

# for i in range(2,3):
#     for j in range(1,11):
#         print(i,'*',j,'=',i*j)
#         # print(f"{i} X {j} = {i*j}")

# for i in range(2,5):
#     for j in range(1,11):
#         print(i,'x',j,'=',i*j)
#         # print(f"{i} X {j} = {i*j}")
#     print()

# for i in range(2,4):
#     for j in range(1,11):
#         if i == j:
#             continue
#         print(i,j)

# square = [i*i for i in range(1,11) if i%2 == 0]
# print(square)

# a = [2,3,4,5]
# res = [val**2 for val in a]
# print(res)

# a = [1,2,3,4,5]
# res = [val for val in a if val%2 == 0]
# print(res)

# a = [1,12,7,10,3,20]
# res = [val for val in a if val > 10]
# print(res)

# a = [i for i in range(10)]
# print(a)

# c = [(x,y) for x in range(1,4) for y in range(1,4)]
# print(c)

# a = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#     ]

# res = [val for row in a for val in row]
# print(res)

# x = 2
# for i in range(1,11):
#     if i%5 == 0:
#         continue
#     print(f"{x} x {i} = {x*i}")

# for i in range(3):
#     print('*',end=' ')

# for i in range(4):
#     for j in range(4):
#         print('*',end=' ')
#     print()

# for i in range(3):
#     for j in range(8):
#         print('*',end=' ')
#     print()

# for i in range(1,6):
#     print('*'*i)

# for i in range(5,0,-1):
#     print('*'*i)

# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# n = 5
# for i in range(n, 0, -1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------