import unittest
from student_manager import StudentManagement
 
class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.sm = StudentManagement()
       
    def test_add_and_view(self):
        self.sm.add_student("Anu", 8, "A")
        self.sm.add_student("Deva", 9, "B")
        self.sm.add_student("Naveen", 7, "C")
        students = self.sm.view_details()
        self.assertEqual(len(students), 3)
       
    def test_search(self):
        student = self.sm.add_student("Anu", 8, "A")
        result = self.sm.search_data(student.student_id)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Anu")
        self.assertEqual(result.age, 8)
        self.assertEqual(result.grade, "A")
       
    def test_delete(self):
        student = self.sm.add_student("Naveen", 7, "C")
        self.sm.add_student("Deva", 9, "B")
        result = self.sm.delete_data(student.student_id)
        self.assertTrue(result)
        self.assertEqual(len(self.sm.view_details()), 1)
       
    def test_delete_nonexistent_data(self):
        result = self.sm.delete_data("non-existent-id")
        self.assertFalse(result)
       
    def tearDown(self):
        return None