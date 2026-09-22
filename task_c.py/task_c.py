import sys
from util import read_numbers

numbers = read_numbers()

if len(numbers) == 0:
    sys.exit("Error: no numbers provided")
a = min(numbers)
b = max(numbers)
c = sum(numbers) / len(numbers)
sorted_nums = sorted(numbers)
n = len(sorted_nums)
mid = n // 2
if n % 2 == 1:
    d = sorted_nums[mid]
else:
    d = (sorted_nums[mid-1] + sorted_nums[mid]) / 2
print(f"Minimum = {a}")
print(f"Maximum = {b}")
print(f"Mean    = {c}")
print(f"Median  = {d}")