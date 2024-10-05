def generate_multiplication_table(number):
    table = []
    for i in range(1, 11):
        table.append(f"{number} x {i} = {number * i}\n")
    return table

def write_table_to_file(number):
    with open("multiplication_table.txt", "w") as file:
        table = generate_multiplication_table(number)
        file.writelines(table)
    print(f"Multiplication table for {number} has been written to 'multiplication_table.txt'.")

number = int(input("Enter a number to generate its multiplication table: "))
write_table_to_file(number)
