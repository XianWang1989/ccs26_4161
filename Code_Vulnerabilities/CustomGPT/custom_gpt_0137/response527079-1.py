
from unittest import TestCase
from unittest.mock import patch, MagicMock

# Assume this is the function we're testing
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Assuming funcToGetBar is something you want to patch
def funcToGetBar():
    # Original implementation here
    pass

class MyTestCase(TestCase):
    @patch('module_containing_funcToGetBar.funcToGetBar')  # Use the correct module path
    def test_get_bar(self, mock_funcToGetBar):
        # Create the mocked bar object
        mocked_bar = MagicMock()

        # This is the value you expect to be returned when accessing the attribute some_attr
        expected_return_value = [obj1, obj2]  # Replace with actual objects

        # Set the return value for some_attr directly on the mocked_bar
        mocked_bar.some_attr = expected_return_value

        # Set the return value of funcToGetBar to be your mocked bar
        mock_funcToGetBar.return_value = mocked_bar

        # Now call foo and assert the result
        self.assertEqual(expected_return_value, foo())

# Remember to define obj1, obj2 or use actual objects for your test
