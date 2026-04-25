
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Assuming this is your function to test
def funcToGetBar():
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(TestCase):
    @patch('__main__.funcToGetBar', return_value=MagicMock())
    def testGetBar(self, mock_func):
        expected_return_val = ['obj1', 'obj2']  # replace with your actual objects
        mocked_bar = mock_func.return_value
        mocked_bar.some_attr = expected_return_val  # Set the attribute directly

        result = foo()
        assert result == expected_return_val  # Use assertEqual as needed

# You can run your tests using a test runner
