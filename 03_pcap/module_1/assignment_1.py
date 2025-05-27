import math

def main():
    print("""
          Select the operation you want to perform:
          1. Factorial
          2. Square root 
          3. Power
          """)
    
    selected_option = input("Enter the number of option: ")
    
    if selected_option == "1":
        input_number = int(input("Enter the number to calculate factorial for: "))
        if input_number < 0:
            print("Negative numbers dont have factorial! ")
            return
        
        print("Factorial:",math.factorial(input_number))
        
        
main()
        
        