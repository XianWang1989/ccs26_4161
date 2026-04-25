
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Assume this is your function to test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTestCase(TestCase):

    @patch('your_module.funcToGetBar')  # Replace 'your_module' with the actual module name
    def testGetBar(self, mock_funcToGetBar):
        # Create a mocked object
        mocked_bar = MagicMock()

        # Set up the expected return value for `some_attr`
        expected_return_val = ['obj1', 'obj2']
        mocked_bar.some_attr = expected_return_val

        # Set the function mock to return the mocked object
        mock_funcToGetBar.return_value = mocked_bar

        # Call the function under test
        result = foo()

        # Assert that the result matches the expected return value
        self.assertEqual(result, expected_return_val)

# If necessary, you can run the tests
if __name__ == '__main__':
    unittest.main()
