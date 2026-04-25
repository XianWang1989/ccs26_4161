
from unittest.mock import MagicMock, patch

# Assume this is your original function
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Here's how you can test it:
expected_return_value = [obj1, obj2]  # your expected return list

@patch('your_module.funcToGetBar')  # Adjust 'your_module' to the actual name
def testGetBar(mock_funcToGetBar):
    mocked_bar = MagicMock()
    mocked_bar.some_attr = expected_return_value  # Directly set 'some_attr'
    mock_funcToGetBar.return_value = mocked_bar  # Patch to return mocked_bar

    # Perform the test
    assert foo() == expected_return_value  # Your assertion

# Run your test
testGetBar()
