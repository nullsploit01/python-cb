user_details = {}

def take_user_details():
    print("Enter your details:")
    user_details['name'] = input("Name: ")
    user_details['age'] = input("Age: ")
    user_details['dob'] = input("Date of Birth: ")
    user_details['email'] = input("Email Address: ")

def show_details():
    if user_details:
        for key, value in user_details.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No details to show.")

def update_details():
    if user_details:
        key = input("Enter the detail you want to update (name, age, dob, email): ").lower()
        if key in user_details:
            new_value = input(f"Enter new {key}: ")
            user_details[key] = new_value
            print("Details updated successfully.")
            show_details()
        else:
            print("Invalid detail.")
    else:
        print("No details available to update.")

def delete_details():
    if user_details:
        key = input("Enter the detail you want to delete (name, age, dob, email): ").lower()
        if key in user_details:
            del user_details[key]
            print("Details deleted successfully.")
            show_details()
        else:
            print("Invalid detail.")
    else:
        print("No details available to delete.")

def main_menu():
    while True:
        print("""
        Choose an option:
        1 -> Add/Enter Details
        2 -> View Details
        3 -> Update Details
        4 -> Delete Details
        5 -> Exit
        """)
        choice = input("Enter your choice: ")
        
        if choice == '1':
            take_user_details()
        elif choice == '2':
            show_details()
        elif choice == '3':
            update_details()
        elif choice == '4':
            delete_details()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

main_menu()