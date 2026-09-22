import sys
from util import read_numbers

numbers = read_numbers()

if len(numbers==0):
    sys.exit("Error: no numbers provided")
Min_val = min(numbers)
Max_val = max(numbers)
Mean_val = sum(numbers) / len(numbers)
a = sorted(numbers)
b = len(a)
mid = b // 2
if b%2==1:
    Median_val=a[mid]
else:
    c=a[mid-1]
    d=a[mid]
    Median_val=(c+d)/2
print(f"Minimum = {Min_val}")
print(f"Maximum = {Max_val}")
print(f"Mean    = {Mean_val}")
print(f"Median  = {Median_val}")