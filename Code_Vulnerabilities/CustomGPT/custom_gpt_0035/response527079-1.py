
from unittest import TestCase
from unittest.mock import MagicMock, patch

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(TestCase):
    @patch('your_module.funcToGetBar')  # replace 'your_module' with the actual module name
    def testGetBar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_val = [obj1, obj2]  # your expected list here

        # Set the attribute on the mock
        mocked_bar.some_attr = expected_return_val
        mock_func.return_value = mocked_bar

        # Execute the function
        result = foo()

        # Assert the expected result
        self.assertEqual(expected_return_val, result)

# Note: Ensure to replace 'obj1', 'obj2', and 'your_module' with your actual objects and module name.
