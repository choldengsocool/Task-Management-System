import unittest

from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)


class TestValidation(unittest.TestCase):
    def test_validate_task_title(self):
        ok, _ = validate_task_title("Valid Title")
        self.assertTrue(ok)
        ok, _ = validate_task_title(123)
        self.assertFalse(ok)
        ok, _ = validate_task_title("")
        self.assertFalse(ok)
        ok, _ = validate_task_title("a" * 101)
        self.assertFalse(ok)

    def test_validate_task_description(self):
        ok, _ = validate_task_description("A description")
        self.assertTrue(ok)
        ok, _ = validate_task_description(123)
        self.assertFalse(ok)
        ok, _ = validate_task_description("")
        self.assertFalse(ok)
        ok, _ = validate_task_description("a" * 501)
        self.assertFalse(ok)

    def test_validate_due_date(self):
        ok, _ = validate_due_date("2099-01-01")
        self.assertTrue(ok)
        ok, _ = validate_due_date("01-01-2099")
        self.assertFalse(ok)
        ok, _ = validate_due_date("2000-01-01")
        self.assertFalse(ok)
        ok, _ = validate_due_date(123)
        self.assertFalse(ok)


if __name__ == "__main__":
    unittest.main()
