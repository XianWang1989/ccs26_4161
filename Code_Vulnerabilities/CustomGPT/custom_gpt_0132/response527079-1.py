
from unittest.mock import MagicMock, patch

def funcToGetBar():
    # This function would typically return some object
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test example
def testGetBar():
    # Create a mock for the bar object
    mocked_bar = MagicMock()
    expected_return_value = [obj1, obj2]  # Replace with actual objects

    # Directly set the attribute on the mocked object
    mocked_bar.some_attr = expected_return_value

    with patch('__main__.funcToGetBar', return_value=mocked_bar):
        result = foo()
        assert result == expected_return_value
