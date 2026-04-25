
from unittest.mock import MagicMock, patch

# The function you're testing
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Assuming funcToGetBar is the function we patch in the test
@patch('your_module.funcToGetBar')  # Adjust the import path accordingly
def testGetBar(mock_func):
    # Create a mock object
    mocked_bar = MagicMock()

    # Expected return value for the 'some_attr' attribute
    expected_return_val = [obj1, obj2]  # Replace with actual objects

    # Assign the expected return value directly to the mock
    mocked_bar.some_attr = expected_return_val

    # Set the return value of the patched function
    mock_func.return_value = mocked_bar

    # Call the function under test
    assert foo() == expected_return_val

# Note: obj1, obj2 should be defined in your actual test
