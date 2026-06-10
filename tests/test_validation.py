import unittest

from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)


class TestValidation(unittest.TestCase):
    def test_validate_task_title(self):
        self.assertTrue(validate_task_title("Valid Title"))
        with self.assertRaises(ValueError):
            validate_task_title(123)
        with self.assertRaises(ValueError):
            validate_task_title("")
        with self.assertRaises(ValueError):
            validate_task_title("a" * 101)

    def test_validate_task_description(self):
        self.assertTrue(validate_task_description("A description"))
        with self.assertRaises(ValueError):
            validate_task_description(123)
        with self.assertRaises(ValueError):
            validate_task_description("")
        with self.assertRaises(ValueError):
            validate_task_description("a" * 501)

    def test_validate_due_date(self):
        self.assertTrue(validate_due_date("2099-01-01"))
        with self.assertRaises(ValueError):
            validate_due_date("01-01-2099")
        with self.assertRaises(ValueError):
            validate_due_date("2000-01-01")
        with self.assertRaises(ValueError):
            validate_due_date(123)


if __name__ == "__main__":
    unittest.main()
