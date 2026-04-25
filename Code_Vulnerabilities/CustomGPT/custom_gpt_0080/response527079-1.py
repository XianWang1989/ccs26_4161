
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Assume this is your function to be tested
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Your test case
class TestFoo(TestCase):
    @patch('module_where_funcToGetBar_is_defined.funcToGetBar')
    def testGetBar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Example expected return value
        mocked_bar.some_attr = expected_return_val  # Directly set the attribute

        mock_func.return_value = mocked_bar  # Patch the function

        # Call the function and assert the results
        self.assertEqual(expected_return_val, foo())
