
from unittest import TestCase
from unittest.mock import MagicMock, patch

def funcToGetBar():
    # Assuming this function is defined elsewhere
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(TestCase):
    @patch('__main__.funcToGetBar')  # Adjust this path to your actual module
    def testGetBar(self, mock_func):
        # Create a MagicMock for the bar object
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Replace with your actual expected values

        # Set the attribute some_attr on the mock object
        mocked_bar.some_attr = expected_return_val

        # Set the return value of funcToGetBar to the mocked bar
        mock_func.return_value = mocked_bar

        # Call foo() and assert the expected return value
        self.assertEqual(expected_return_val, foo())

if __name__ == '__main__':
    unittest.main()
