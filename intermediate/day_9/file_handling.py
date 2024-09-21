# open("file.txt", "w") -> Create a file
# open("file.txt", "r") -> Read from a file
# open("file.txt", "a") -> append a file
# open("file.txt", "r+") -> Read, write

# take user's name, city, state, country and store it in a file
# name: {name}
# city: {city}
# state: {state}
# country: {country}

name = input("Name: ")
city = input("city: ")
state = input("state: ")
country = input("country: ")

with open("user.txt", "w") as user_file:
    user_file.writelines([
        f"name: {name}\n",
        f"city: {city}\n",
        f"state: {state}\n",
        f"country: {country}\n",
    ])