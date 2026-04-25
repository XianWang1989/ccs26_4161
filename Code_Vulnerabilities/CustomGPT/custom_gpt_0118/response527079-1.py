
from unittest.mock import MagicMock, patch

# Your function under test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test case
@patch('your_module.funcToGetBar')  # Adjust the import path
def testGetBar(mocked_funcToGetBar):
    mocked_bar = MagicMock()
    expected_return_val = ['obj1', 'obj2']  # Example list

    # Set the attribute directly on the mock object
    mocked_bar.some_attr = expected_return_val

    # Mock funcToGetBar to return the mocked bar
    mocked_funcToGetBar.return_value = mocked_bar

    # Assert that the function returns the expected value
    assert foo() == expected_return_val

# Run the test
if __name__ == '__main__':
    import unittest
    unittest.main()
