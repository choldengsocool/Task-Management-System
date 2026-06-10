import unittest
import tempfile
import os

from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
    save_tasks,
    load_tasks,
    tasks,
)


class TestTaskUtils(unittest.TestCase):
    def setUp(self):
        tasks.clear()

    def tearDown(self):
        tasks.clear()

    def test_add_task_success(self):
        ok, _ = add_task("Task 1", "Desc", "2099-01-01")
        self.assertTrue(ok)
        self.assertEqual(len(tasks), 1)

    def test_add_task_invalid_due(self):
        ok, _ = add_task("Task 2", "Desc", "2000-01-01")
        self.assertFalse(ok)

    def test_mark_task_complete(self):
        add_task("T", "D", "2099-01-02")
        ok, _ = mark_task_as_complete(1)
        self.assertTrue(ok)
        self.assertTrue(tasks[0]["completed"])

    def test_view_pending_tasks(self):
        add_task("a", "b", "2099-01-01")
        add_task("c", "d", "2099-01-02")
        mark_task_as_complete(1)
        pending = view_pending_tasks()
        self.assertEqual(len(pending), 1)
        self.assertEqual(pending[0]["title"], "c")

    def test_calculate_progress(self):
        tasks.clear()
        add_task("a", "b", "2099-01-01")
        add_task("c", "d", "2099-01-02")
        mark_task_as_complete(2)
        progress = calculate_progress()
        self.assertEqual(progress, 50)

    def test_save_load_tasks(self):
        tasks.clear()
        add_task("persist", "x", "2099-12-31")
        fd, fname = tempfile.mkstemp(prefix="tasks_", suffix=".json")
        os.close(fd)
        try:
            save_tasks(fname)
            tasks.clear()
            ok, msg = load_tasks(fname)
            self.assertTrue(ok)
            self.assertEqual(len(tasks), 1)
            self.assertEqual(tasks[0]["title"], "persist")
        finally:
            try:
                os.remove(fname)
            except OSError:
                pass


if __name__ == "__main__":
    unittest.main()
