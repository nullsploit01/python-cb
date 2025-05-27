import writer.writer 

filename = "system_report.txt"
print(writer.writer.read_lines_of_data(filename))

filename = "custom_file.txt"
writer.writer.write_lines_of_data(filename, ["Hello!\n", "I am write via writer module.\n"])