
from unittest.mock import MagicMock, patch

# The function you want to test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test case
@patch('your_module.funcToGetBar')
def testGetBar(mock_funcToGetBar):
    # Set up the mocked bar object
    mocked_bar = MagicMock()

    # Set the return_value of the attribute directly
    expected_return_val = [obj1, obj2]  # Put actual objects here
    mocked_bar.some_attr = expected_return_val

    # Patch funcToGetBar to return the mocked object
    mock_funcToGetBar.return_value = mocked_bar

    # Call the function and assert the expected value
    assert foo() == expected_return_val
