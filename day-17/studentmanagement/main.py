#main.py — CLI Interface
# main.py
from student_manager import StudentManager
from student import Student
 
def print_menu():
    print("\n--- Student Management System ---")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student by ID")
    print("4. Delete student")
    print("5. Exit")
 
def main():
    manager = StudentManager()
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()
 
        if choice == "1":
            student_id = input("Enter student ID: ").strip()
            name = input("Enter student name: ").strip()
            age_input = input("Enter age: ").strip()
            grade = input("Enter grade: ").strip()
            try:
                age = int(age_input)
                student = Student(student_id, name, age, grade)
                manager.add_student(student)
                print("Student added successfully!")
            except ValueError as ve:
                print("Error:", ve)
 
        elif choice == "2":
            students = manager.view_students()
            if not students:
                print("No students found.")
            else:
                print("\nList of Students:")
                for student in students:
                    print(student)
 
        elif choice == "3":
            student_id = input("Enter student ID to search: ").strip()
            student = manager.search_student(student_id)
            if student:
                print("Student found:")
                print(student)
            else:
                print("Student not found.")
 
        elif choice == "4":
            student_id = input("Enter student ID to delete: ").strip()
            if manager.delete_student(student_id):
                print("Student deleted successfully!")
            else:
                print("Student not found. Could not delete.")
 
        elif choice == "5":
            print("Exiting Student Management System. Goodbye!")
            break
 
        else:
            print("Invalid choice. Please select a valid option.")
 
if __name__ == "__main__":
    main()
 