
from unittest import TestCase
from unittest.mock import MagicMock, patch

# This is your function under test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(TestCase):
    @patch('your_module.funcToGetBar')  # Adjust 'your_module' to the actual module name
    def testGetBar(self, mock_func):
        # Create the mock object
        mocked_bar = MagicMock()
        expected_return_val = [obj1, obj2]  # Your expected return value

        # Set the attribute directly on the mocked_bar
        mocked_bar.some_attr = expected_return_val

        # Set the return value of the patched function
        mock_func.return_value = mocked_bar  

        # Call the function and assert the result
        result = foo()
        self.assertEqual(expected_return_val, result)

# Run the tests
if __name__ == "__main__":
    import unittest
    unittest.main()
