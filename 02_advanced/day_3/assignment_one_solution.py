number = int(input("Enter a number: "))

multiplication = lambda x, y: x * y

for i in range(1, 11):
    print(f"{number} x {i} = {multiplication(number, i)}")