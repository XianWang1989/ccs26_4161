
from unittest.mock import MagicMock, patch

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Assuming funcToGetBar exists in the same module
@patch('__main__.funcToGetBar')
def testGetBar(mocked_func):
    mocked_bar = MagicMock()
    expected_return_val = ['obj1', 'obj2']  # Example expected return value

    mocked_bar.some_attr = expected_return_val
    mocked_func.return_value = mocked_bar  # Patch funcToGetBar to return mocked_bar

    assert foo() == expected_return_val

# Run the test
testGetBar()
print("Test passed!")
