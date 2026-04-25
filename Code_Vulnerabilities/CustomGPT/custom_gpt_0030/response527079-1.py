
from unittest.mock import MagicMock, patch

# Assuming foo is in a module named my_module
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test case
@patch('my_module.funcToGetBar')
def testGetBar(mocked_func):
    # Create a MagicMock for the returned bar object
    mocked_bar = MagicMock()
    # Expected return value for the attribute
    expected_return_val = ['obj1', 'obj2']
    # Set some_attr to return the expected value
    mocked_bar.some_attr = expected_return_val  # Directly set the attribute

    # Set the mock function to return the mocked_bar
    mocked_func.return_value = mocked_bar

    # Call the function under test
    result = foo()

    # Assert the result
    assert result == expected_return_val

# Run the test
testGetBar()
