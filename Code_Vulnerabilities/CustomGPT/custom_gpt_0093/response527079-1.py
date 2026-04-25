
from unittest import TestCase
from unittest.mock import MagicMock, patch

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(TestCase):
    @patch('__main__.funcToGetBar')  # Adjust the import path as necessary
    def testGetBar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']
        mocked_bar.some_attr = expected_return_val  # Directly set the attribute
        mock_func.return_value = mocked_bar  # Patch the function

        self.assertEqual(expected_return_val, foo())  # Assert the expected value

if __name__ == '__main__':
    unittest.main()
