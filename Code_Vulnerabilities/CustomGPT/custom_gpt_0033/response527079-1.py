
from unittest.mock import MagicMock, patch
import pytest

# Assuming your function foo is in a module named your_module
# from your_module import foo

def funcToGetBar():
    # Your actual implementation here
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

@pytest.fixture
def mock_func_to_get_bar():
    with patch('__main__.funcToGetBar') as mocked_func:
        yield mocked_func

def test_get_bar(mock_func_to_get_bar):
    mocked_bar = MagicMock()
    expected_return_val = ['obj1', 'obj2']  # Your expected return value
    mocked_bar.some_attr = expected_return_val  # Set the attribute directly
    mock_func_to_get_bar.return_value = mocked_bar  # Mock the function call

    # Call the function
    result = foo()

    # Assert the result matches the expected return value
    assert result == expected_return_val
