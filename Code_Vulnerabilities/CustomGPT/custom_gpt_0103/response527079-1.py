
from unittest.mock import MagicMock, patch

# Your function
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Example test case
class TestFoo:
    @patch('__main__.funcToGetBar')  # Adjust the import path as needed
    def test_get_bar(self, mock_func):
        # Create a mocked bar object
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Change as needed

        # Set the 'some_attr' attribute on the mocked bar
        mocked_bar.some_attr = expected_return_val
        mock_func.return_value = mocked_bar  # Patching funcToGetBar

        # Call the function under test
        result = foo()

        # Assert the result
        assert result == expected_return_val
