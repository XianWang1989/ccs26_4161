
from unittest.mock import MagicMock, patch

# Your function
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# The test
@patch('your_module.funcToGetBar')  # Replace 'your_module' with the actual module name
def testGetBar(mock_funcToGetBar):
    # Create a mock object for bar
    mocked_bar = MagicMock()
    expected_return_val = [obj1, obj2]  # Define your expected return value

    # Set the some_attr attribute directly on the mocked bar
    mocked_bar.some_attr = expected_return_val

    # Set the return value of funcToGetBar to be the mocked bar
    mock_funcToGetBar.return_value = mocked_bar

    # Call the function under test
    result = foo()

    # Assert that the result is as expected
    assert result == expected_return_val
