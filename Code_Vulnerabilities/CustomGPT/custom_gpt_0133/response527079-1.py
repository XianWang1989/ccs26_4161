
from unittest.mock import MagicMock, patch

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

def test_get_bar():
    mocked_bar = MagicMock()
    expected_return_val = ['obj1', 'obj2']  # Example expected return value
    # Patch the function that returns the "bar" object
    with patch('__main__.funcToGetBar', return_value=mocked_bar):
        # Set the `some_attr` attribute directly on the mocked object
        mocked_bar.some_attr = expected_return_val

        # Call the function under test
        result = foo()

        # Assert the result is what you expect
        assert result == expected_return_val

# Example of running the test
test_get_bar()
