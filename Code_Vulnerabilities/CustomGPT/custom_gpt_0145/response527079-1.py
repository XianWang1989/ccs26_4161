
from unittest.mock import MagicMock, patch

# Assuming this function is defined somewhere in your code
def funcToGetBar():
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Your test case
expected_return_val = [obj1, obj2]  # Your expected return value

@patch('__main__.funcToGetBar')  # Adjust the import path as necessary
def testGetBar(mocked_func):
    mocked_bar = MagicMock()
    mocked_bar.some_attr = expected_return_val  # Set the attribute directly
    mocked_func.return_value = mocked_bar  # Set the return value of the patched function

    assert foo() == expected_return_val  # Now it should work correctly

# You can call testGetBar() or use a test runner like pytest or unittest
