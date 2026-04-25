
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Your function that you want to test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Your test case
class TestFoo(TestCase):
    @patch('your_module.funcToGetBar')  # Adjust the import path accordingly
    def test_get_bar(self, mocked_func):
        # Prepare the expected return value
        expected_return_value = ['obj1', 'obj2']

        # Create a MagicMock for bar
        mocked_bar = MagicMock()

        # Set the some_attr attribute directly on the mock
        mocked_bar.some_attr = expected_return_value

        # Set the return value of funcToGetBar to be the mocked_bar
        mocked_func.return_value = mocked_bar

        # Assert that foo returns the expected value
        self.assertEqual(expected_return_value, foo())

# Running the tests
if __name__ == '__main__':
    import unittest
    unittest.main()
