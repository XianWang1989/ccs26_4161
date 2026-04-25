
from unittest.mock import MagicMock, patch

# Assuming this is your function
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Your test
expected_return_val = [obj1, obj2]  # Replace with your actual objects
mocked_bar = MagicMock()
mocked_bar.some_attr = expected_return_val  # Set the attribute directly

with patch('path.to.funcToGetBar', return_value=mocked_bar):
    def testGetBar():
        assert expected_return_val == foo()

# Run the test
testGetBar()
