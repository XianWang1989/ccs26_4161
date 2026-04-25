
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Assuming your actual function looks something like this:
def funcToGetBar():
    # This function would normally return some object
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(TestCase):

    @patch('your_module.funcToGetBar')  # Update with the correct module path
    def test_get_bar(self, mock_func):
        expected_return_val = [obj1, obj2]  # Your expected list of objects
        mocked_bar = MagicMock()
        mocked_bar.some_attr = expected_return_val  # Set the attribute directly

        mock_func.return_value = mocked_bar  # Patch the function to return the mock

        # Call the function under test
        result = foo()

        # Assert the result is as expected
        self.assertEqual(result, expected_return_val)

# In your test runner, ensure you call tests in this TestCase.
