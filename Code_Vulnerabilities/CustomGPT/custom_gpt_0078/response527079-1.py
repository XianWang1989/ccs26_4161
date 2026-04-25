
from unittest.mock import MagicMock, patch
import unittest

def funcToGetBar():
    # This is just a placeholder for the actual function that gets 'bar'.
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(unittest.TestCase):

    @patch('__main__.funcToGetBar')  # Adjust the patch target based on your module
    def testGetBar(self, mock_funcToGetBar):
        mocked_bar = MagicMock()
        expected_return_val = [1, 2, 3]  # Example expected return value
        mocked_bar.some_attr = expected_return_val  # Directly set the 'some_attr' attribute
        mock_funcToGetBar.return_value = mocked_bar

        result = foo()
        self.assertEqual(expected_return_val, result)

if __name__ == '__main__':
    unittest.main()
