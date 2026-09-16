import sys
from util import read_numbers
numbers=read_numbers
if len(numbers==0):
    sys.exit("Error:no numbers provided")
Maximum=max(numbers)
Minimum=min(numbers)
Mean=sum(numbers)/len(numbers)
a=sorted(numbers)
b=len(a)
if b%2==1:
    Median=a[b//2]
else:
    c=a[b//2-1]
    d=a[b//2]
    Median=(c+d)/2
print(f"Minimum={Minimum}")
print(f"Maximum={Maximum}")
print(f"Mean={Mean}")
print(f"Median={Median}")