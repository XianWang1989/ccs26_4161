
from unittest.mock import MagicMock, patch

# Original function
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test function
@patch('path.to.funcToGetBar')  # Adjust the import path
def testGetBar(mock_func):
    # Create a mock object
    mocked_bar = MagicMock()
    expected_return_val = [obj1, obj2]  # Replace with your actual objects

    # Set the attribute directly
    mocked_bar.some_attr = expected_return_val
    mock_func.return_value = mocked_bar  # Patch funcToGetBar

    # Run the function under test
    result = foo()

    # Assert the result
    assert result == expected_return_val
