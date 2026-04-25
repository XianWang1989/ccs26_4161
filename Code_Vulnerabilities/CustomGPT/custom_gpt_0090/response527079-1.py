
from unittest import TestCase
from unittest.mock import patch, MagicMock

# Your function
def funcToGetBar():
    # This is your placeholder function
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(TestCase):
    @patch('__main__.funcToGetBar')
    def testGetBar(self, mock_funcToGetBar):
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Your expected return value
        mocked_bar.some_attr = expected_return_val  # Set the attribute directly

        mock_funcToGetBar.return_value = mocked_bar  # Patch the function

        result = foo()
        self.assertEqual(result, expected_return_val)  # Assert the expected result

# To run the test
if __name__ == '__main__':
    import unittest
    unittest.main()
