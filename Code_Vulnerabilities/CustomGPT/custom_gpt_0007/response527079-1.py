
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Assume funcToGetBar is imported from your module
# from your_module import funcToGetBar

class MyTestCase(TestCase):

    @patch('your_module.funcToGetBar')  # Adjust the import path accordingly
    def testGetBar(self, mock_funcToGetBar):
        # Create a mock object
        mocked_bar = MagicMock()
        expected_return_value = ['obj1', 'obj2']  # Example expected value

        # Set the attribute directly on the mocked object
        mocked_bar.some_attr = expected_return_value

        # Configure the mocked function to return the mocked bar
        mock_funcToGetBar.return_value = mocked_bar  

        # Call the function under test
        result = foo()  # Assuming 'foo' is defined elsewhere in your module

        # Assert the result is as expected
        self.assertEqual(expected_return_value, result)

