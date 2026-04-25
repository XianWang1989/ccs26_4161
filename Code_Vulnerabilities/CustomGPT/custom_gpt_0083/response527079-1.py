
from unittest.mock import MagicMock, patch

# Assume this is your function to be tested
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Your test case
@patch('your_module.funcToGetBar')  # Adjust to your actual module path
def testGetBar(mock_func):
    mocked_bar = MagicMock()
    expected_return_val = ["obj1", "obj2"]  # Example objects

    # Set the attribute directly on the mock object
    mocked_bar.some_attr = expected_return_val
    mock_func.return_value = mocked_bar  # Patch funcToGetBar

    # Execute the function
    result = foo()

    # Assert the result
    assert result == expected_return_val

# Call the test function
testGetBar()
