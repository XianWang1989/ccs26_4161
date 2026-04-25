
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Assume this is your function
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Your test case
class TestFoo(TestCase):
    @patch('your_module.funcToGetBar')  # Replace 'your_module' with the actual module name
    def test_get_bar(self, mock_func):
        # Set up the mock
        mocked_bar = MagicMock()
        expected_return_val = [obj1, obj2]  # Replace with your actual objects

        # Directly set 'some_attr' on the mock
        mocked_bar.some_attr = expected_return_val

        # Assign the mock to the patched function
        mock_func.return_value = mocked_bar

        # Call the function and assert
        assert expected_return_val == foo()

# Remember to define your obj1, obj2 for the test
