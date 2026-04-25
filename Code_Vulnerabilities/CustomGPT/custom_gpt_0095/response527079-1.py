
from unittest import TestCase
from unittest.mock import MagicMock, patch

# Assuming this is your function to be tested
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class MyTest(TestCase):

    @patch('your_module.funcToGetBar')  # Adjust the module name accordingly
    def testGetBar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_value = ['obj1', 'obj2']

        # Set the attribute directly on the mock
        setattr(mocked_bar, 'some_attr', expected_return_value)
        mock_func.return_value = mocked_bar  # Patch funcToGetBar

        # Call the function under test
        result = foo()

        # Assert that the result is as expected
        self.assertEqual(result, expected_return_value)

if __name__ == '__main__':
    unittest.main()
