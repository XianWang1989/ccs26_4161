
from unittest.mock import MagicMock, patch

# Your original function
def foo():
    bar = funcToGetBar()
    return bar.some_attr  # changed from getattr to direct attribute access

# Test Case
@patch('your_module.funcToGetBar')  # replace 'your_module' with where funcToGetBar is defined
def testGetBar(self, mock_func_to_get_bar):
    mocked_bar = MagicMock()
    expected_return_val = [obj1, obj2, ...]
    mocked_bar.some_attr = expected_return_val  # Set the attribute directly
    mock_func_to_get_bar.return_value = mocked_bar  # Patch the function to return the mocked object

    assert expected_return_val == foo()  # Here we can directly call foo
