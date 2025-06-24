try:
    try:
        x = int(input("Enter a number: "))
        print(10 / x)
        
    except ZeroDivisionError as z:
        print("Inner Exception:", z)
        
    except ValueError as v:
        print("Inner Exception:", v)
        
except ValueError as v:
    print("Outer Exception:", v)
        
        