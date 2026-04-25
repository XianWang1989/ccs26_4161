
from unittest import TestCase
from unittest.mock import patch, MagicMock

# The function you are testing
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test case
class MyTestCase(TestCase):

    @patch('path.to.funcToGetBar')  # Adjust the import path accordingly
    def test_get_bar(self, mock_func):
        # Create a mock object for bar
        mocked_bar = MagicMock()

        # Set the expected return value for some_attr
        expected_return_val = ['obj1', 'obj2']
        mocked_bar.some_attr = expected_return_val

        # Set the return value of funcToGetBar to mocked_bar
        mock_func.return_value = mocked_bar

        # Call the function under test
        result = foo()

        # Assert the result is as expected
        self.assertEqual(expected_return_val, result)

# Run the tests
if __name__ == '__main__':
    unittest.main()
