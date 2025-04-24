# student_manager.py
from student import Student
from storage import load_data, save_data
 
class StudentManager:
    def __init__(self):
        # Initialize the student list by reading the JSON file.
        self.students = load_data()
 
    def add_student(self, student):
        """Add a new student if the ID is unique."""
        if self.search_student(student.student_id):
            raise ValueError("Student with this ID already exists.")
        self.students.append(student)
        save_data(self.students)
 
    def view_students(self):
        """Return the list of students."""
        return self.students
 
    def search_student(self, student_id):
        """Search and return a student by their ID."""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
 
    def delete_student(self, student_id):
        """Delete a student by their ID."""
        student = self.search_student(student_id)
        if student:
            self.students.remove(student)
            save_data(self.students)
            return True
        return False