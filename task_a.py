import sys
a=input("Enter an integer form 1 to 100")
try:
    b=int(a)
except ValueError:
    sys.exit("Error:Grade must be an integer between 1 and 100")
if b<0 or b>100:
    sys.exit("Error:Grade must be an integer between 1 and 100")
if b>=0 and b<=39:
    print("{b} is a Fail")
elif b>=40 and b<=69:
    print("{b} is a Pass")
elif b>=70 and b<=100:
    print("{b} is a Distinction")