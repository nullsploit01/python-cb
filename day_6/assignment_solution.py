balance = 0.0

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"${amount} deposited successfully.")
    else:
        print("Deposit amount must be positive.")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance.")
    elif amount <= 0:
        print("Withdrawal amount must be positive.")
    else:
        balance -= amount
        print(f"${amount} withdrawn successfully.")

def check_balance():
    print(f"Your current balance is: ${balance}")

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")                   
        
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            withdraw(amount)
        elif choice == '3':
            check_balance()
        elif choice == '4':
            print("Thank you for using the banking system.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

main_menu()