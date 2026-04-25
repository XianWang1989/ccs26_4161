
from unittest import TestCase
from unittest.mock import patch, MagicMock

# Assuming this is your function under test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test case
class MyTestCase(TestCase):
    @patch('__main__.funcToGetBar')  # Adjust the patch target as necessary
    def testGetBar(self, mock_func):
        # Create a mock object for bar
        mocked_bar = MagicMock()
        expected_return_val = [obj1, obj2]  # Your expected return value
        mocked_bar.some_attr = expected_return_val  # Set the attribute directly

        mock_func.return_value = mocked_bar  # Make funcToGetBar return the mocked bar

        # Call your function and assert the expected output
        self.assertEqual(expected_return_val, foo())

# If using directly in a script, you can run with:
if __name__ == '__main__':
    import unittest
    unittest.main()
