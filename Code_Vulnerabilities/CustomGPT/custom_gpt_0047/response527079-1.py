
from unittest.mock import MagicMock, patch

# Assume funcToGetBar is part of a class/module you can patch
@patch('module_containing_func.funcToGetBar')  # Adjust the path to your actual function
def test_get_bar(mocked_func):
    # Create a mock for the bar object
    mocked_bar = MagicMock()

    # Set the expected return value directly on the mock for the desired attribute
    expected_return_val = [obj1, obj2]  # Replace obj1, obj2 with actual objects
    mocked_bar.some_attr = expected_return_val  # Use some_attr directly

    # Configure the patched function to return the mocked bar
    mocked_func.return_value = mocked_bar

    # Call the function being tested
    result = foo()

    # Assert the expected result matches the actual result
    assert result == expected_return_val
