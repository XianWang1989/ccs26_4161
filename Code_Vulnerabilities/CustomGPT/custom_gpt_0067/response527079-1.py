
from unittest.mock import patch, MagicMock
import unittest

def funcToGetBar():
    # This function would normally retrieve the 'bar' object
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(unittest.TestCase):
    @patch('__main__.funcToGetBar')  # Adjust the path according to your module structure
    def testGetBar(self, mocked_func):
        # Arrange
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']
        mocked_func.return_value = mocked_bar

        # Set up the mock to return the expected value for the attribute 'some_attr'
        mocked_bar.some_attr = expected_return_val

        # Act
        result = foo()

        # Assert
        self.assertEqual(expected_return_val, result)

if __name__ == '__main__':
    unittest.main()
