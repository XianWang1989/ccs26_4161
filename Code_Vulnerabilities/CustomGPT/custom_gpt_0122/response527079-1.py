
from unittest import TestCase
from unittest.mock import patch, MagicMock

# Your function to test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Function to be mocked
def funcToGetBar():
    # This would return some object in real use
    pass

# Test case
class TestFoo(TestCase):
    @patch('__main__.funcToGetBar')
    def test_get_bar(self, mock_funcToGetBar):
        # Mocking the bar object
        mocked_bar = MagicMock()
        expected_return_value = ['obj1', 'obj2']

        # Set the return value of the 'some_attr' attribute
        mocked_bar.some_attr = expected_return_value
        mock_funcToGetBar.return_value = mocked_bar  # Patch the function

        # Call the function
        result = foo()

        # Assert the result
        self.assertEqual(result, expected_return_value)

# To run the test
if __name__ == '__main__':
    import unittest
    unittest.main()
