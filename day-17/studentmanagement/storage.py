# storage.py
import json
import os
from student import Student
 
FILE_PATH = "students.json"
 
def load_data():
    """Load students data from the JSON file."""
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        try:
            data = json.load(f)
            # Convert dictionaries to Student objects
            return [Student.from_dict(item) for item in data]
        except json.JSONDecodeError:
            return []
 
def save_data(students):
    """Save students data to the JSON file."""
    with open(FILE_PATH, "w") as f:
        # Convert Student objects to dictionaries
        data = [student.to_dict() for student in students]
        json.dump(data, f, indent=4)