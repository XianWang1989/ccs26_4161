
from unittest.mock import patch, MagicMock

# Your function under test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Example test case
def testGetBar():
    expected_return_val = [obj1, obj2]  # Your expected value
    mocked_bar = MagicMock()
    mocked_bar.some_attr = expected_return_val  # Set the attribute directly

    with patch('your_module.funcToGetBar', return_value=mocked_bar):
        result = foo()
        assert result == expected_return_val  # Use assert for testing

# Ensure you replace 'your_module' with the actual module where funcToGetBar is defined.
