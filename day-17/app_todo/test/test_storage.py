import unittest
import os
from storage import Storage

class TestStorage(unittest.TestCase):

    def setUp(self):
        self.filepath = 'test_tasks.json'
        self.storage = Storage(self.filepath)

    def test_save_and_load(self):
        task_list = [
            {"id": "1", "description": "Task 1", "completed": False},
            {"id": "2", "description": "Task 2", "completed": True}
        ]
        self.storage.save(task_list)
        loaded = self.storage.load()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0]['id'], "1")
        self.assertEqual(loaded[1]['id'], "2")
        self.assertEqual(loaded[0]['description'], "Task 1")
        self.assertEqual(loaded[1]['description'], "Task 2")
        self.assertEqual(loaded[0]['completed'], False)
        self.assertEqual(loaded[1]['completed'], True)

    def tearDown(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)