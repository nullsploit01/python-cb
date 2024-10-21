students = {
 'Fpnmg': [15, 10, 15, 9, 1],
 'Ieyhn': [23, 9, 6, 14, 10],
 'Auvsb': [25, 7, 5, 21, 2],
 'Omwza': [3, 23, 4, 5, 14],
 'Htmze': [9, 7, 20, 7, 2],
 'Eweyf': [23, 25, 24, 14, 21],
 'Wtbkq': [4, 15, 19, 27, 5],
 'Zdhgr': [26, 27, 11, 22, 20],
 'Ecezq': [3, 25, 12, 21, 13],
 'Pybia': [11, 9, 8, 12, 22],
 'Ivwfr': [25, 10, 29, 9, 1],
 'Ccpit': [26, 13, 29, 15, 20],
 'Hxvbi': [23, 4, 27, 8, 20],
 'Kaimb': [16, 10, 13, 22, 10],
 'Twkkc': [12, 3, 2, 8, 5],
 'Fzolm': [25, 7, 27, 1, 23],
 'Qyxfh': [22, 18, 9, 0, 11],
 'Hwvhh': [3, 17, 19, 23, 14],
 'Hartc': [12, 28, 20, 0, 6],
 'Dkomm': [5, 26, 27, 9, 7],
 'Nqnqj': [26, 25, 29, 3, 12],
 'Bafkn': [0, 0, 1, 0, 25],
 'Ailvs': [7, 27, 5, 4, 5],
 'Psowg': [15, 8, 1, 10, 24],
 'Kxlun': [18, 21, 5, 22, 12],
 'Zxlqo': [17, 16, 30, 26, 29],
 'Upxoy': [3, 18, 26, 11, 0],
 'Kcvxr': [5, 15, 25, 8, 27],
 'Uzugx': [24, 29, 18, 4, 18],
 'Adduz': [7, 30, 29, 9, 11]
}


def average_marks_subject(subject_index):
    total = sum(students[student][subject_index] for student in students)
    return total / len(students)

def average_marks_all_students():
    averages = {student: sum(marks) / len(marks) for student, marks in students.items()}
    return averages

def sort_students_by_subject(subject_index, descending=False):
    return sorted(students.items(), key=lambda x: x[1][subject_index], reverse=descending)

def console_app():
    while True:
        print("\nOptions:")
        print("1. Average marks of students in a specific subject")
        print("2. Average marks of each student across all subjects")
        print("3. Sort students by marks in a specific subject")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            subject_index = int(input("Enter subject index (0-4): "))
            average = average_marks_subject(subject_index)
            print(f"Average marks in subject {subject_index + 1}: {average:.2f}")
        
        elif choice == '2':
            averages = average_marks_all_students()
            for student, avg in averages.items():
                print(f"{student}: {avg:.2f}")
        
        elif choice == '3':
            subject_index = int(input("Enter subject index (0-4): "))
            order = input("Sort ascending or descending (asc/desc)?: ")
            descending = order.lower() == 'desc'
            sorted_students = sort_students_by_subject(subject_index, descending)
            for student, marks in sorted_students:
                print(f"{student}: {marks[subject_index]}")
        
        elif choice == '4':
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

console_app()