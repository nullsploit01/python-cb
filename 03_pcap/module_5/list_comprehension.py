# list = [1, 2, 3, 4, 5]
# ans = []
# for n in list:
#     ans.append(n ** 2)
    
# print(ans)

squares = [x ** 2 for x in range(1, 6)]
print(squares)

even_squares = [x ** 2 for x in range(1, 6) if x % 2 == 0]
print(even_squares)

# create a list that has a list of numbers from 1 to 100 divisible by 3
# a list if tuples like (x, x ** 2) for eg [(1, 1), (2, 4), (3, 9)...]