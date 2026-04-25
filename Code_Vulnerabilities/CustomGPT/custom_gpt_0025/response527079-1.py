
from unittest.mock import MagicMock, patch

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Example test
expected_return_val = [obj1, obj2]

@patch('your_module.funcToGetBar')  # Adjust the module path accordingly
def test_get_bar(mocked_func):
    mocked_bar = MagicMock()
    mocked_bar.some_attr = expected_return_val  # Set the attribute directly
    mocked_func.return_value = mocked_bar       # Patch the return value of funcToGetBar

    result = foo()

    assert result == expected_return_val  # Assert the result
