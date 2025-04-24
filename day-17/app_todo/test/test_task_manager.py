import unittest
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.tm = TaskManager()

    def test_add_and_get_tasks(self):
        self.tm.add_task("Task 1")
        self.tm.add_task("Task 2")
        tasks = self.tm.get_all_tasks()
        self.assertEqual(len(tasks), 2)

    def test_complete_task(self):
        task = self.tm.add_task("Task 1")
        result = self.tm.complete_task(task.id)
        self.assertTrue(result)
        self.assertTrue(task.completed)

    def test_delete_task(self):
        task = self.tm.add_task("Task 1")
        result = self.tm.delete_task(task.id)
        self.assertTrue(result)
        self.assertEqual(len(self.tm.get_all_tasks()), 0)

    def test_delete_nonexistent_task(self):
        result = self.tm.delete_task("non-existent-id")
        self.assertFalse(result)

    def tearDown(self):
        return None