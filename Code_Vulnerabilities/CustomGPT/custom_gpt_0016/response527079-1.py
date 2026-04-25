
from unittest.mock import MagicMock, patch
import unittest

# Assume this is the function you want to test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(unittest.TestCase):

    @patch('__main__.funcToGetBar')  # Adjust the path based on where funcToGetBar is defined
    def testGetBar(self, mock_func):
        # Create a MagicMock object
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Example expected return value

        # Set the 'some_attr' directly on the mock object
        mocked_bar.some_attr = expected_return_val  # Assign the list to some_attr
        mock_func.return_value = mocked_bar  # funcToGetBar returns mocked_bar

        # Call the function and assert the result
        self.assertEqual(expected_return_val, foo())

if __name__ == '__main__':
    unittest.main()
