
from unittest import TestCase
from unittest.mock import patch, MagicMock

# Assume funcToGetBar is defined elsewhere
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(TestCase):
    @patch('module.path.to.funcToGetBar')  # Update the path to funcToGetBar
    def testGetBar(self, mock_funcToGetBar):
        # Create a MagicMock instance for bar
        mocked_bar = MagicMock()
        expected_return_val = [obj1, obj2]  # Replace with actual objects

        # Set the attribute directly on the mocked object
        mocked_bar.some_attr = expected_return_val

        # Patch funcToGetBar to return the mocked bar
        mock_funcToGetBar.return_value = mocked_bar

        # Call the function and assert the expected return value
        self.assertEqual(expected_return_val, foo())
