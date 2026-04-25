
from unittest.mock import MagicMock, patch

def testGetBar(self):
    mocked_bar = MagicMock()
    expected_return_val = [obj1, obj2]  # Replace with actual objects

    # You can simply set the attribute directly on the mocked object
    mocked_bar.some_attr = expected_return_val

    with patch('your_module.funcToGetBar', return_value=mocked_bar):
        result = foo()
        assert result == expected_return_val
