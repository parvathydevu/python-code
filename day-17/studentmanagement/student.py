# first code to  print 
import json
 
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id  # Unique identifier
        self.name = name
        self.age = age
        self.grade = grade
 
    def to_dict(self):
        """Convert the student instance to a dictionary."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }
 
    @classmethod
    def from_dict(cls, data):
        """Create a student instance from a dictionary."""
        return cls(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            grade=data["grade"]
        )
 
    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
 