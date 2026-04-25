
from unittest.mock import MagicMock, patch

# Your function under test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test case
expected_return_val = [obj1, obj2]  # Assuming obj1 and obj2 are defined somewhere

@patch('module_where_funcToGetBar_is.funcToGetBar')
def testGetBar(mocked_func):
    mocked_bar = MagicMock()

    # Set the attribute directly on the mocked_bar
    mocked_bar.some_attr = expected_return_val

    # Set the return value of the patched function
    mocked_func.return_value = mocked_bar

    # Call the function and assert the expected result
    assert foo() == expected_return_val
