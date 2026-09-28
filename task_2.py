x = input("What should I call you?")
print(f"Greetings, welcome to our savings tool {x}!")
y = input("How much will you deposit each month?")
try:
    int(y)
    z = int(y) * 12
    print({z},"This is total money")
    total = z * 1.008
    print(f"With interest,you will save £{total:.2f} per year")
except:
    print("Invalid amount")
