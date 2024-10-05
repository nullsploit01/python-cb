# number % 3 = FIZZ
# number % 5 = BUZZ
# number % 3 and number % 5 = FIZZBUZZ
# number is not divisible by 3 OR 5 = NO_LUCK
# LOGICAL OPERANDS -> and, or, not

number = 15

if number % 3 == 0 and number % 5 == 0:
    print("FIZZBUZZ")

elif number % 5 == 0:
    print("Buzz")

elif number % 3 ==0:
    print("FIZZ")

else:
    print("NO LUCK")
