
from unittest.mock import MagicMock, patch

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Assuming this is part of your test case
@patch('path.to.your.module.funcToGetBar')  # Update with the correct path
def testGetBar(mock_funcToGetBar):
    # Create a mock for bar
    mocked_bar = MagicMock()

    # Set the desired return value for some_attr
    expected_return_val = [obj1, obj2]  # Example objects
    mocked_bar.some_attr = expected_return_val

    # Patch funcToGetBar to return the mocked_bar
    mock_funcToGetBar.return_value = mocked_bar

    # Call foo and assert the returned value
    assert foo() == expected_return_val
