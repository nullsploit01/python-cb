def check_age(age):
    if int(age) < 0:
        raise ValueError("Age cannot be negative")
    
    print("Age is valid")
    
try:
    check_age("a")
    
except ValueError as v:
    print(v)
    
except Exception as e:
    print(e)
    
finally:
    print("Closing program..")