
from unittest import TestCase
from unittest.mock import patch, MagicMock

# Function to test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test class
class TestMyFunction(TestCase):

    @patch('your_module.funcToGetBar')  # Adjust the import path accordingly
    def testGetBar(self, mocked_func):
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # your expected return values

        # Set the attribute directly on the mock object
        mocked_bar.some_attr = expected_return_val

        mocked_func.return_value = mocked_bar  # Patch the function to return our mock

        # Call your function and assert
        self.assertEqual(expected_return_val, foo())

# Running the test
if __name__ == '__main__':
    unittest.main()
