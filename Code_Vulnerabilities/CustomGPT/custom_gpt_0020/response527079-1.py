
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Assume the code you're testing is in a module named 'my_module'
# from my_module import foo  

class MyTestCase(TestCase):

    @patch('my_module.funcToGetBar')  # Ensure you patch where funcToGetBar is being imported
    def testGetBar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Replace with your actual expected values
        # Set the attribute directly on mocked_bar
        mocked_bar.some_attr = expected_return_val
        mock_func.return_value = mocked_bar  # funcToGetBar is patched

        # Call the function under test
        result = foo()

        # Assert that the result matches the expected return value
        self.assertEqual(result, expected_return_val)

# To run the tests, you would typically use this:
if __name__ == '__main__':
    from unittest import main
    main()
