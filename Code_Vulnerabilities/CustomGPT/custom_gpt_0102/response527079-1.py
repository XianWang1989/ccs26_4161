
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Assume this is the function to test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test class
class MyTestCase(TestCase):
    @patch('path.to.funcToGetBar')
    def test_get_bar(self, mock_func):
        # Create a mock object for bar
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']

        # Set the attribute directly on the mock object
        mocked_bar.some_attr = expected_return_val

        # Set the mock function to return our mocked bar
        mock_func.return_value = mocked_bar

        # Call foo and assert the result
        result = foo()
        self.assertEqual(result, expected_return_val)

# Run the test
if __name__ == "__main__":
    import unittest
    unittest.main()
