
from unittest import TestCase
from unittest.mock import patch, MagicMock

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(TestCase):
    @patch('your_module.funcToGetBar')  # Adjust the module path accordingly
    def test_get_bar(self, mock_func):
        # Create a mock object
        mocked_bar = MagicMock()
        expected_return_val = [obj1, obj2]  # Your expected return values

        # Set the expected attribute directly on the mocked_bar
        mocked_bar.some_attr = expected_return_val
        mock_func.return_value = mocked_bar  # Patch the function

        # Call the function under test
        result = foo()

        # Assert the result is as expected
        self.assertEqual(expected_return_val, result)
