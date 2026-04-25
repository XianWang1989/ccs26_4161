
from unittest import TestCase
from unittest.mock import patch, MagicMock

# Assuming this is your existing function defined somewhere
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(TestCase):
    @patch('your_module.funcToGetBar')  # replace 'your_module' with your actual module name
    def testGetBar(self, mock_func):
        # Create your mock object
        mocked_bar = MagicMock()
        expected_return_val = [obj1, obj2]  # your expected return value

        # Set the attribute directly on the mocked bar object
        mocked_bar.some_attr = expected_return_val

        # Set the return value of the patched function
        mock_func.return_value = mocked_bar 

        # Assert that the function returns the correct value
        self.assertEqual(expected_return_val, foo())
