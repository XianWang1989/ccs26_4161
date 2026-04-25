
from unittest.mock import MagicMock, patch

# Your function definition
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test case
@patch('your_module_name.funcToGetBar')
def test_get_bar(mocked_func):
    mocked_bar = MagicMock()
    expected_return_val = ['obj1', 'obj2']  # your expected return value
    # Set the some_attr attribute directly on the mocked_bar
    mocked_bar.some_attr = expected_return_val
    mocked_func.return_value = mocked_bar  # funcToGetBar is patched to return mocked_bar

    # Call the function and assert the expected outcome
    assert foo() == expected_return_val
