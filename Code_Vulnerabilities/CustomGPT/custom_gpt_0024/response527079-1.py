
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Assume funcToGetBar is defined elsewhere
def funcToGetBar():
    # This function should return an object with an attribute
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(TestCase):

    @patch('__main__.funcToGetBar')  # Adjust the path according to your module
    def testGetBar(self, mocked_func):
        # Create a mock for the bar object
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Your expected return value

        # Set the expected return value directly as an attribute
        mocked_bar.some_attr = expected_return_val
        mocked_func.return_value = mocked_bar  # Patch the funcToGetBar to return mocked_bar

        # Call foo and assert the result
        result = foo()
        self.assertEqual(expected_return_val, result)

# If you're running this script, you can run the tests with:
# if __name__ == '__main__':
#     unittest.main()
