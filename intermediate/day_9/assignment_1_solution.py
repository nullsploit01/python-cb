def save_user_data(user_data):
    with open("user_data.txt", "w") as file:
        for key, value in user_data.items():
            file.write(f"{key}: {value}\n")

def read_user_data():
    try:
        with open("user_data.txt", "r") as file:
            print("\nCurrent User Data:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("\nNo data available. Please add user information.")

def get_user_input():
    user_data = {}
    user_data['Name'] = input("Enter your name: ")
    user_data['Phone'] = input("Enter your phone number: ")
    user_data['City'] = input("Enter your city: ")
    user_data['State'] = input("Enter your state: ")
    user_data['Country'] = input("Enter your country: ")
    user_data['Age'] = input("Enter your age: ")
    user_data['DOB'] = input("Enter your date of birth (DD/MM/YYYY): ")
    return user_data

def update_user_data(user_data):
    field = input("\nEnter the field to update (Name, Phone, City, State, Country, Age, DOB): ")
    if field in user_data:
        user_data[field] = input(f"Enter new value for {field}: ")
    else:
        print(f"{field} is not a valid field.")
    return user_data

def remove_user_data():
    try:
        open("user_data.txt", "w").close()
        print("\nUser data removed.")
    except FileNotFoundError:
        print("\nNo data found to remove.")


while True:
    print("\nMenu:")
    print("1. Add User Data")
    print("2. View User Data")
    print("3. Update User Data")
    print("4. Remove User Data")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        user_data = get_user_input()
        save_user_data(user_data)
        print("\nUser data saved.")
    elif choice == '2':
        read_user_data()
    elif choice == '3':
        try:
            with open("user_data.txt", "r") as file:
                user_data = {}
                lines = file.readlines()
                for line in lines:
                    key, value = line.strip().split(": ")
                    user_data[key] = value
            user_data = update_user_data(user_data)
            save_user_data(user_data)
            print("\nUser data updated.")
        except FileNotFoundError:
            print("\nNo data available. Please add user information first.")
    elif choice == '4':
        remove_user_data()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
