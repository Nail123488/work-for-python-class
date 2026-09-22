import sys

try:
    grade = int(input("Enter grade: "))
except ValueError:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if grade < 0 or grade > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if grade >= 70:
    result = "Distinction"
elif grade >= 40:
    result = "Pass"
else:
    result = "Fail"

print(f"{grade} is a {result}")
