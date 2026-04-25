
from unittest.mock import MagicMock, patch

# Let's say this is the function you want to test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Example test case
@patch('your_module.funcToGetBar')  # Adjust the import path accordingly
def test_get_bar(mock_func):
    # Create a MagicMock object
    mocked_bar = MagicMock()
    expected_return_value = ['obj1', 'obj2']  # Replace this with your actual expected values

    # Set the 'some_attr' attribute directly on the mocked object
    mocked_bar.some_attr = expected_return_value

    # Set the return value of the patched function
    mock_func.return_value = mocked_bar  

    # Assert that the function returns the expected value
    assert foo() == expected_return_value
