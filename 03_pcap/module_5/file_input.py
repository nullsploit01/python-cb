with open("file.txt", "w") as file:
    file.write("Hello World!")
    
with open("file.txt", "r") as file:
    content = file.read()
    print(content)
    
# take input from user append it in a file
# write multiple lines from user as input in a file