def write_data(filename, data):
    with open(filename, "w") as file:
        file.write(data)
        
def write_lines_of_data(filename, data):
    with open(filename, "w") as file:
        file.writelines(data)
        
def read_data(filename):
    with open(filename, "r") as file:
        return file.read()
    
def read_lines_of_data(filename):
    with open(filename, "r") as file:
        return file.readlines()
    