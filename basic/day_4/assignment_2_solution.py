year = int(input("Enter a year: "))

if year < 0:
    print("Invalid Year")

else:
    if year % 4 == 0:
        print("Its a Leap Year!")
    else:
        print("Its Not a Leap Year!")