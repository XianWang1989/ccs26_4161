
from unittest import mock
import unittest

# The function you want to test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Function to be patched
def funcToGetBar():
    pass  # This would normally return an object

class TestFoo(unittest.TestCase):
    @mock.patch('__main__.funcToGetBar')
    def test_get_bar(self, mock_func):
        # Setup the mock
        mocked_bar = mock.MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Your expected result

        # Set the some_attr attribute directly
        mocked_bar.some_attr = expected_return_val

        # Set the return value of funcToGetBar to the mocked bar
        mock_func.return_value = mocked_bar

        # Call the function under test
        result = foo()

        # Assert the result is what you expect
        self.assertEqual(expected_return_val, result)

if __name__ == '__main__':
    unittest.main()
