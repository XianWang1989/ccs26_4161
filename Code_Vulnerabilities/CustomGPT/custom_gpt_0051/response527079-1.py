
from unittest import TestCase
from unittest.mock import MagicMock, patch

def funcToGetBar():
    # This function would normally return a bar object.
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(TestCase):
    @patch('__main__.funcToGetBar')
    def testGetBar(self, mock_func):
        # Create a MagicMock for the bar object
        mocked_bar = MagicMock()
        expected_return_val = ["obj1", "obj2"]  # Example expected return value

        # Set the some_attr attribute directly on the mocked_bar
        mocked_bar.some_attr = expected_return_val

        # Patch funcToGetBar to return the mocked_bar
        mock_func.return_value = mocked_bar

        # Call foo and assert the expected value
        self.assertEqual(expected_return_val, foo())

# Run the tests
if __name__ == '__main__':
    import unittest
    unittest.main()
