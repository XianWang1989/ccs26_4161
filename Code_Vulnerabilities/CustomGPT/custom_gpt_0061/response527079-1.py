
from unittest.mock import MagicMock, patch

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# In your test
mocked_bar = MagicMock()
expected_return_val = [obj1, obj2]  # Replace with your actual objects
mocked_bar.some_attr = expected_return_val  # Directly set the attribute

with patch('your_module.funcToGetBar', return_value=mocked_bar):  # Replace 'your_module' with the actual module
    def testGetBar(self):
        assert foo() == expected_return_val
