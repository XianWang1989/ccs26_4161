
from unittest.mock import MagicMock, patch

# Assuming funcToGetBar is the function being patched
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

def testGetBar():
    # Mocking the function that returns bar
    mock_bar = MagicMock()
    expected_return_val = ['obj1', 'obj2']

    # Set the attribute on the mock object directly
    mock_bar.some_attr = expected_return_val

    with patch('path.to.funcToGetBar', return_value=mock_bar):
        assert foo() == expected_return_val
