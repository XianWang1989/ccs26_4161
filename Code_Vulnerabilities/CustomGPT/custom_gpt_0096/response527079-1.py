
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Your original function
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class YourTestCase(TestCase):
    @patch('your_module.funcToGetBar')
    def testGetBar(self, mock_func):
        # Setup
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']

        # Set the attribute directly
        mocked_bar.some_attr = expected_return_val
        mock_func.return_value = mocked_bar

        # Execute
        result = foo()

        # Verify
        self.assertEqual(expected_return_val, result)
