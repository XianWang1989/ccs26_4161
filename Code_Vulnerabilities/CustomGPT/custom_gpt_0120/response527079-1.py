
from unittest import TestCase
from unittest.mock import patch, MagicMock

# Function to be tested
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test case
class TestFoo(TestCase):

    @patch('your_module.funcToGetBar')  # Replace 'your_module' with the actual module name
    def test_get_bar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_val = [obj1, obj2]  # Your expected return value

        # Set the attribute 'some_attr' directly on the mocked bar object
        mocked_bar.some_attr = expected_return_val

        # Set funcToGetBar's return value
        mock_func.return_value = mocked_bar

        # Call the function and assert the result
        result = foo()
        self.assertEqual(result, expected_return_val)
