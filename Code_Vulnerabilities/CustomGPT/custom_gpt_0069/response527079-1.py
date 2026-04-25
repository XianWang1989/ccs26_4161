
from unittest.mock import MagicMock, patch

# Your function definition
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test function
@patch('your_module.funcToGetBar')  # Replace 'your_module' with the actual module name
def testGetBar(mocked_func):
    mocked_bar = MagicMock()
    expected_return_val = [obj1, obj2]  # Replace with actual objects

    # Set the return value of funcToGetBar
    mocked_func.return_value = mocked_bar

    # Directly assign the attribute
    mocked_bar.some_attr = expected_return_val

    # Run your function under test
    result = foo()

    # Assert that the result is as expected
    assert result == expected_return_val
