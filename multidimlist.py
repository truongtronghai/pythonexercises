import numpy as np
import pandas as pd

ml = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

# Using Panda for Multi-dimensional list
df = pd.DataFrame(ml)

print(df)
print("========== Using Pandas ============")

sum_all = df.sum().sum()
print(f"Sum of all numbers: {sum_all}")

print("=========")
counting_number = df.count(axis="columns").sum()
print(f"Average of all numbers: {'{:.2f}'.format(sum_all / counting_number)}")

print("=========")
# print(df.mask(df % 2 != 0, 0))
sum_of_even_number = df.mask(df % 2 != 0, 0).sum().sum()
print(f"Sum of all even numbers: {sum_of_even_number}")

print("=========")
df_even_number = df.mask(df % 2 != 0, None)
##print(df_even_number)
counting_even_number = df_even_number.count(axis="columns").sum()

print(f"Average of all even numbers: {sum_of_even_number / counting_even_number}")

print("========== Using Python, no Pandas ============")
sum_all = 0
counting_number = 0

for l in ml:
    for item in l:
        sum_all += item
        counting_number += 1

print(f"Sum of all numbers: {sum_all}")
print("=========")
print(f"Average of all numbers: {'{:.2f}'.format(sum_all / counting_number)}")

sum_of_even_number = 0
counting_even_number = 0

for l in ml:
    for item in l:
        if item % 2 == 0:
            sum_of_even_number += item
            counting_even_number += 1

print("=========")
print(f"Sum of all even numbers: {sum_of_even_number}")
print("=========")
print(f"Average of all even numbers: {sum_of_even_number / counting_even_number}")
