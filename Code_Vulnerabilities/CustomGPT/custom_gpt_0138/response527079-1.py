
from unittest.mock import MagicMock, patch
import pytest

# Your function
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test case
@patch('your_module.funcToGetBar')  # Adjust the import path as needed
def testGetBar(mock_func):
    mocked_bar = MagicMock()
    expected_return_val = ['obj1', 'obj2']  # Example list

    # Directly set the attribute on the mock
    mocked_bar.some_attr = expected_return_val
    mock_func.return_value = mocked_bar

    # Run the function and assert
    assert foo() == expected_return_val
