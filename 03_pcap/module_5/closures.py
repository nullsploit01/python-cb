def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)

print(add_five(6))

# write a closure that returns a function which multiplies its argument by 7