# Initializing Dictionary
student_grades = {}

# Add a new student
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a grade of {grade}")

# Update a student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s grade has been updated to {grade}")
    else:
        print(f"{name} is not found!")

# Delete a student(for delete a student we just need its key)
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found!")

# View all students
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students found/added")

# Main function
def main():
    while True:
        print('\nStudent Grade Management System')
        print('1. Add Student')
        print('2. Update Student')
        print('3. Delete Student')
        print('4. View All Students')
        print('5. Exit')

        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            name = input("Enter student name: ")
            grade = input("Enter student grade (e.g., A, B, 90): ")  # Accept string or number
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name: ")
            grade = input("Enter updated student grade (e.g., A, B, 90): ")  # Accept string or number
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 5.")

main()
