
from unittest.mock import MagicMock, patch

# Assuming obj1 and obj2 are defined somewhere
obj1 = "object1"
obj2 = "object2"
expected_return_val = [obj1, obj2]

@patch('path.to.funcToGetBar')
def testGetBar(mock_func):
    # Create the mock object
    mocked_bar = MagicMock()

    # Set 'some_attr' directly on the mocked object
    mocked_bar.some_attr = expected_return_val

    # Configure the mock to return the mocked_bar
    mock_func.return_value = mocked_bar

    # Call the function and assert the return value
    result = foo()

    assert result == expected_return_val
