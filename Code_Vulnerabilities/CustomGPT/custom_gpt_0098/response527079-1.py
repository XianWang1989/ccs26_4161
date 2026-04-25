
from unittest import TestCase
from unittest.mock import MagicMock, patch

def funcToGetBar():
    # This will be mocked in the test
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(TestCase):
    @patch('__main__.funcToGetBar')  # adjust if funcToGetBar is in a different module
    def testGetBar(self, mock_func):
        # Create a mock object
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']

        # Set 'some_attr' directly on mocked_bar
        mocked_bar.some_attr = expected_return_val
        mock_func.return_value = mocked_bar  # funcToGetBar is patched

        result = foo()  # Call the function under test

        self.assertEqual(expected_return_val, result)  # Compare with expected return value

# To run the tests you would typically use a test runner like pytest or unittest.
