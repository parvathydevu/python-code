import unittest
from task import Task

class Testtask(unittest.TestCase):
    def test_task_creation(self):
        t = Task("Test Task")
        # testing the initial condition of the created task
        self.assertEqual(t.description, "Test Task")
        self.assertFalse(t.completed)

    def test_mark_completed(self):
        t = Task("Test")
        t.mark_completed()
        self.assertEqual(t.completed, True)

    def test_to_dict_and_from_dict(self):
        t1 = Task("Test Task")
        d = t1.to_dict()
        t2 = Task.from_dict(d)
        self.assertEqual(t1.id, t2.id)
        self.assertEqual(t1.description, t2.description)
        self.assertEqual(t1.completed, t2.completed)

if __name__ == "__main__":

    unittest.main()
