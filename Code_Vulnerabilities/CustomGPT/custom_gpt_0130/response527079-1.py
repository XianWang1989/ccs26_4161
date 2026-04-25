
from unittest.mock import MagicMock, patch

# Assuming foo is already defined in your module
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test case
@patch('your_module.funcToGetBar')  # Adjust the import path as needed
def test_get_bar(mock_func):
    mocked_bar = MagicMock()
    expected_return_val = ['obj1', 'obj2']  # Your expected return value

    # Set the attribute directly on the mocked object
    mocked_bar.some_attr = expected_return_val
    mock_func.return_value = mocked_bar  # Patch funcToGetBar to return mocked_bar

    # Call your function and assert the result
    assert foo() == expected_return_val
