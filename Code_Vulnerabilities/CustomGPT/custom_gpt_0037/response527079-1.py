
from unittest.mock import MagicMock, patch

# Assume funcToGetBar is defined elsewhere
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

expected_return_val = [obj1, obj2]  # Replace with your actual expected values

@patch('your_module.funcToGetBar')  # patch the function where it's used
def test_get_bar(mock_func):
    mocked_bar = MagicMock()
    mocked_bar.some_attr = expected_return_val  # Set the attribute directly
    mock_func.return_value = mocked_bar  # Mock the return value of the function

    assert foo() == expected_return_val  # Assert the expected output
