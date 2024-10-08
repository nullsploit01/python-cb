try:
    print('reading a file')
    with open("file.txt", "r") as file:
        print(file.read())

    print('updating object')
    some_object = {2: 1}
    some_object[2] += 1

    print('reading array')
    some_list = []
    print(some_list[0])

except FileNotFoundError:
    print("FileNotFoundError error occured, processing it")
    with open("file.txt", "w") as file:
        file.write("test data")

except KeyError:
    print("KeyError error occured, ignoring it")

except:
    print("unknown error")