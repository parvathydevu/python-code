import unittest
from student import Students

class TestStudent(unittest.TestCase):

    def test_student_creation(self):
        t = Students("Test Student", 20, "A")
        self.assertEqual(t.name, "Test Student")
        self.assertEqual(t.age, 20)
        self.assertEqual(t.grade, "A")

    def test_to_dict_and_from_dict(self):
        t1 = Students("Test Student", 20, "A")
        d = t1.to_dict()
        t2 = Students.from_dict(d)
        self.assertEqual(t1.name, t2.name)
        self.assertEqual(t1.age, t2.age)
        self.assertEqual(t1.grade, t2.grade)

if __name__ == "__main__":
    unittest.main()


