import sys
from util import read_numbers

numbers = read_numbers()
if len(numbers==0):
    sys.exit("Error: no numbers provided")
Maximum = max(numbers)
Minimum = min(numbers)
Mean = sum(numbers) / len(numbers)
a = sorted(numbers)
b = len(a)
mid = b // 2
if b%2==1:
    Median=a[mid]
else:
    c=a[mid-1]
    d=a[mid]
    Median=(c+d)/2
print(f"Minimum = {Minimum}")
print(f"Maximum = {Maximum}")
print(f"Mean    = {Mean}")
print(f"Median  = {Median}")