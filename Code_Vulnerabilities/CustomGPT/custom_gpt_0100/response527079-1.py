
from unittest.mock import MagicMock, patch

# Assume funcToGetBar is defined somewhere in your module

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test
expected_return_val = [obj1, obj2]  # Replace with your actual objects

@patch('your_module.funcToGetBar')
def testGetBar(mocked_func):
    # Create a MagicMock for bar
    mocked_bar = MagicMock()

    # Set the 'some_attr' attribute directly on the mocked_bar
    mocked_bar.some_attr = expected_return_val

    # Patch funcToGetBar to return the mocked_bar
    mocked_func.return_value = mocked_bar

    # Assert the function returns the expected value
    assert foo() == expected_return_val

# Run the test
testGetBar()
