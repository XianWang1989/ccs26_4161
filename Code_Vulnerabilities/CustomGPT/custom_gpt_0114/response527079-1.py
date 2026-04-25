
from unittest.mock import MagicMock, patch

# The function to be tested
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test case
class TestFoo:
    @patch('__main__.funcToGetBar')  # Adjust the path according to your module
    def test_get_bar(self, mock_func):
        # Create the mocked bar object
        mocked_bar = MagicMock()

        # Define the expected return value
        expected_return_val = ['obj1', 'obj2']

        # Set the attribute directly on the mocked_bar
        mocked_bar.some_attr = expected_return_val

        # Set the return value of the mocked function
        mock_func.return_value = mocked_bar  

        # Call the function
        result = foo()

        # Assert the result
        assert result == expected_return_val

# To run the test, use a test runner like pytest or unittest.
