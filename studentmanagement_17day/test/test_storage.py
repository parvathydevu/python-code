import unittest
import os
from storage import Storage
 
class TestStorage(unittest.TestCase):
    def setUp(self):
        self.filepath = 'test_students.json'
        self.storage = Storage(self.filepath)
       
    def testing_save_load(self):      
        student_list = [
            {"Student_ID": 1, "Name": "Adithya", "Age": 6, "Grade": "A"},
            {"Student_ID": 2, "Name": "Deva", "Age": 7, "Grade": "B"},
            {"Student_ID": 3, "Name": "Sarah", "Age": 8, "Grade": "C"},
            {"Student_ID": 4, "Name": "Sid", "Age": 9, "Grade": "A"}
        ]
       
        self.storage.save(student_list)
        loaded = self.storage.load()
        self.assertEqual(len(loaded), 4)
        self.assertEqual(loaded[0]['Student_ID'], 1)
        self.assertEqual(loaded[1]['Name'], "Deva")
        self.assertEqual(loaded[2]['Age'], 8)
        self.assertEqual(loaded[3]['Grade'], "A")
       
    def tearDown(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)