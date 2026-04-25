
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Assume this is your original function
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(TestCase):

    @patch('your_module.funcToGetBar')  # Replace 'your_module' with the actual module name
    def testGetBar(self, mocked_func):
        # Create the mock object
        mocked_bar = MagicMock()

        # Define the expected return value
        expected_return_val = ['obj1', 'obj2']

        # Set the attribute directly on the mocked bar
        mocked_bar.some_attr = expected_return_val

        # Set the return value of the patched function
        mocked_func.return_value = mocked_bar

        # Execute the function and assert
        result = foo()
        self.assertEqual(expected_return_val, result)

# If you want to actually run the test case
if __name__ == "__main__":
    import unittest
    unittest.main()
