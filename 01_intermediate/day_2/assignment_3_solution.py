def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for number in array:
    print(f"Is {number} a prime number? {is_prime(number)}")