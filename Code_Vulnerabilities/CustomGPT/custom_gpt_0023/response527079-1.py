
from unittest.mock import MagicMock, patch

def funcToGetBar():
    # This function would normally return an object
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

def testGetBar():
    # The expected return value from foo
    expected_return_val = [obj1, obj2]

    # Create a mock object
    mocked_bar = MagicMock()

    # Set the return value of the specific attribute
    mocked_bar.some_attr = expected_return_val

    # Patch funcToGetBar to return our mocked object
    with patch('__main__.funcToGetBar', return_value=mocked_bar):
        result = foo()
        assert result == expected_return_val

# To run the test
testGetBar()
