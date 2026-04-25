
from unittest.mock import MagicMock, patch

# Assume this is your function you want to test
def funcToGetBar():
    # The implementation is not relevant for the test
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)


# Now let's write the test
expected_return_val = ['obj1', 'obj2']  # Your desired return value

# Patch the funcToGetBar function
@patch('__main__.funcToGetBar')  # Adjust the patch target according to your module
def testGetBar(mocked_func):
    # Create a mock object for bar
    mocked_bar = MagicMock()

    # Set the attribute `some_attr` on the mocked bar
    mocked_bar.some_attr = expected_return_val

    # Configure the mocked function to return the mocked bar
    mocked_func.return_value = mocked_bar

    # Call the function and assert
    assert foo() == expected_return_val

# Running the test
if __name__ == '__main__':
    testGetBar()
