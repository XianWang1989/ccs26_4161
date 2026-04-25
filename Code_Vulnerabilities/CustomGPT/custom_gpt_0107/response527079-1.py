
from unittest.mock import MagicMock, patch

# Assume foo is defined as in your question
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Your test case
class TestMyFunction:
    @patch('path.to.your.module.funcToGetBar')
    def testGetBar(self, mock_func):
        # Set up the expected return value
        expected_return_val = [obj1, obj2]  # Replace with actual objects

        # Create a MagicMock and set the some_attr attribute
        mocked_bar = MagicMock()
        mocked_bar.some_attr = expected_return_val

        # Set the return value of funcToGetBar to the mocked bar
        mock_func.return_value = mocked_bar

        # Assert that foo returns the expected value
        assert foo() == expected_return_val
