
from unittest.mock import MagicMock, patch

# Assuming funcToGetBar is defined somewhere

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

@patch('your_module.funcToGetBar')  # Use the correct module path
def testGetBar(mocked_func):
    mocked_bar = MagicMock()
    expected_return_val = [obj1, obj2]  # Replace with your actual objects

    # Set the mock's attribute directly
    mocked_bar.some_attr = expected_return_val
    mocked_func.return_value = mocked_bar  # Patch funcToGetBar

    # Call the function and assert
    assert expected_return_val == foo()
