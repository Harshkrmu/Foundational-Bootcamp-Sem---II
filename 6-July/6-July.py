import numpy as np

# arr = np.array([1,2,3], dtype = np.int32)

# arr1 = np.array([1,2,3,4])
# arr2 = np.array([1,2,3,4])
# print(arr1+arr2)

# arr = np.array([1,4,9,16])
# print(np.sqrt(arr))

# arr = np.array([1,2,3,4,5])
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.median(arr))

# arr = np.array([[1,2,3],[4,5,6]])
# print(arr.reshape((3,2)))

# arr1 = np.array([1,2,3])
# arr2 = np.array([[1],[2],[3]])
# print(arr1+arr2)

# arr1 = np.array([1,2,3,4,5])
# bool_idx = arr1 > 3
# print(bool_idx)
# print(arr1[bool_idx])

# arr1 = np.array([[1,2],[3,4]])
# arr2 = np.array([[5,6],[7,8]])
# print(np.dot(arr1,arr2))

# arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
# print(np.std(arr1))
# print(np.var(arr1))

# arr1 = np.array([1,2,3,4,5])
# print(np.percentile(arr1,50))
# print(np.quantile(arr1,0.25))

# arr1 = np.array([1,2,3,4,5])
# print(np.cumsum(arr1))
# print(np.cumprod(arr1))

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# print(np.corrcoef(arr1,arr2))
# print(np.cov(arr1,arr2))

# # Problem 1

# n = np.arange(1,21)
# arr = (n**2+1).reshape(4,5)
# print(arr)

# db = arr*2
# print(db)

# d5 = arr%5 == 0
# print(np.sum(d5))

# mod_arr = arr
# mod_arr[d5] = -1
# print(mod_arr)

# # Problem 2

# arr = np.arange(1,101).reshape(10,10)
# print(arr)

# pr_row = arr[[1,2,4,6]]
# print(pr_row)

# rev_com = arr
# rev_com[:,:1:2] = rev_com[::-1,:1:2]
# print(rev_com)

# diag = arr
# np.fill_diagonal(diag,0)
# print(diag)

# top = arr[0,:]
# bottom = arr[-1,:]
# left = arr[1:-1,0]
# right = arr[1:-1,-1]

# border_sum = np.sum(top)+np.sum(bottom)+np.sum(left)+np.sum(right)
# print(border_sum)

# rotated = np.rot90(arr,-1)
# print(rotated)

# # Problem 3

# np.random.seed(42)
# arr = np.random.randint(1, 501, 1000)
# print(arr)

# perf_sq = np.sqrt(arr) % 1 == 0
# perf_sqcount = np.sum(perf_sq)
# print(perf_sqcount)

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(np.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
# prime = np.array([is_prime(num) for num in arr])
# prime_count = np.sum(prime)
# print(prime_count)

# mod_arr = arr.astype(float)
# mul_of_7 = mod_arr % 7 == 0
# mod_arr[mul_of_7] = np.sqrt(mod_arr[mul_of_7])
# print(mod_arr)

# sort_arr = np.sort(arr)
# gaps = np.diff(sort_arr)
# larg_gap = np.max(gaps)
# print(larg_gap)
# cum_sum = np.cumsum(arr)
# print(cum_sum)

# index = np.argmax(cum_sum > 100000)
# print(index)
# print(cum_sum[index])

# # Problem 4 

# np.random.seed(42)
# arr = np.random.randint(50, 251, size=(30, 5))

# print("Patient Data:\n")
# print(arr)

# mean = np.mean(arr, axis=0)
# print("\nDepartment-wise Mean:")
# print(mean)

# median = np.median(arr, axis=0)
# print("\nDepartment-wise Median:")
# print(median)

# std = np.std(arr, axis=0)
# print("\nDepartment-wise Standard Deviation:")
# print(std)

# highest_day = np.argmax(arr, axis=0) + 1
# highest_value = np.max(arr, axis=0)

# print("\nHighest Patient Day:")
# for i in range(5):
#     print(f"Department {i+1}: Day {highest_day[i]} ({highest_value[i]} arr)")

# lowest_day = np.argmin(arr, axis=0) + 1
# lowest_value = np.min(arr, axis=0)
# print("\nLowest Patient Day:")
# for i in range(5):
#     print(f"Department {i+1}: Day {lowest_day[i]} ({lowest_value[i]} arr)")

# lower = mean - 2 * std
# upper = mean + 2 * std

# outliers = (arr < lower) | (arr > upper)
# print("\nOutlier Positions (Day, Department):")
# positions = np.argwhere(outliers)
# print(positions)

# updated = arr.astype(float)
# for col in range(5):
#     updated[outliers[:, col], col] = mean[col]
# print("\nData after Replacing Outliers:")
# print(updated)

import pandas as pd

# data = {1:"frt",2:"fef",3:"er"}
# data = [10,20,30,40]
# series = pd.Series(data)
# print(series)
# print(series[0])

# print(series.max())
# print(series.describe())

# data = {
#     'Name': ['John', 'Anna', 'Peter', 'Linda'],
#     'Age' : [28,24,35,32],
#     'City' : ['New York', 'Paris', 'Berlin', 'London']
# }

# df = pd.DataFrame(data)
# print(df)