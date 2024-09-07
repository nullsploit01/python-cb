# Take user details from user, (name, age, DOB, email)
# Store it in a dictionary
# Ask user what they wanna know? name, age, DOB, email and show them
# Ask user if they want to change any details

user_details = {}

def take_user_details():
    name = input("Name: ")
    user_details['name'] = name

    age = input("Age: ")
    user_details['age'] = age

    DOB = input("Date of Birth: ")
    user_details['dob'] = DOB

    email = input("Email Address: ")
    user_details['email'] = email


def show_details_prompt():
    user_input = input("""
    What do you want to know?
    1 -> Name
    2 -> Age
    3 -> Date of Birth
    4 -> Email                       
""")
    
    if user_input == "1":
        print(user_details['name'])

    elif user_input == "2":
        print(user_details["age"])
    
    elif user_input == "3":
        print(user_details['dob'])

    elif user_input == "4":
        print(user_details['email'])

    else:
        print("invalid choice")

def show_update_prompt():
    user_input = input("""
    What do you want to change?
    1 -> Name
    2 -> Age
    3 -> Date of Birth
    4 -> Email                       
""")
    
    if user_input == "1":
        print(f"current name: {user_details['name']}")
        name = input("Updated Name: ")
        user_details['name'] = name

    elif user_input == "2":
        print(f"current age: {user_details['age']}")
        age = input("Updated age: ")
        user_details['age'] = age
    
    elif user_input == "3":
        print(f"current date of birth: {user_details['dob']}")
        dob = input("Updated dob: ")
        user_details['dob'] = dob

    elif user_input == "4":
        print(f"current email: {user_details['email']}")
        email = input("Updated email: ")
        user_details['email'] = email

    else:
        print("invalid choice")
        return
    
    print(f"Updated Details {user_details}")

take_user_details()
show_details_prompt()
show_update_prompt()