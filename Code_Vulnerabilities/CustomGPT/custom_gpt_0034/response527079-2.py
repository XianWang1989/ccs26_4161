
from unittest.mock import MagicMock, patch
import unittest

class MyTestCase(unittest.TestCase):

    @patch('your_module.funcToGetBar')  # Change 'your_module' to the actual module name
    def test_get_bar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_val = [obj1, obj2]  # Replace with actual objects
        mocked_bar.some_attr = expected_return_val  # Set the attribute directly

        mock_func.return_value = mocked_bar  # Patch the function to return the mocked object

        result = foo()  # Call the function under test
        self.assertEqual(result, expected_return_val)  # Check the result

if __name__ == "__main__":
    unittest.main()
