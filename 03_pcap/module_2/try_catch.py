try:
    x = int(input("Enter a number: "))
    print(10 / x)
    
except ZeroDivisionError:
    print("Cannot divide by 0 ")
    
except ValueError:
    print("Number should be int")
    
except Exception:
    print("Error occured")

else:
    print("division was successful!")
    
finally:
    print("closing program...")
    
    
# x = int(input("Enter a number: "))
# print(10 / x)