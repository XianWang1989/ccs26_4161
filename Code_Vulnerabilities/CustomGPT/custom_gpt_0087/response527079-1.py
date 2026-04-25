
from unittest.mock import MagicMock, patch

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test code
def testGetBar(self):
    mocked_bar = MagicMock()
    expected_return_val = [obj1, obj2]  # Example expected return value
    mocked_bar.some_attr = expected_return_val  # Directly setting the attribute

    with patch('module_name.funcToGetBar', return_value=mocked_bar):
        result = foo()
        assertEqual(result, expected_return_val)  # Ensure the values match
