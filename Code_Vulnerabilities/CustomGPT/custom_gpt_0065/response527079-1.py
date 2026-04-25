
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Sample function to test
def funcToGetBar():
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(TestCase):
    @patch('__main__.funcToGetBar')  # Adjust the import path as necessary
    def test_get_bar(self, mocked_func_to_get_bar):
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']

        # Set the attribute directly on the mock
        mocked_bar.some_attr = expected_return_val
        mocked_func_to_get_bar.return_value = mocked_bar

        # Call the function and assert the expected result
        result = foo()
        self.assertEqual(result, expected_return_val)

if __name__ == '__main__':
    unittest.main()
