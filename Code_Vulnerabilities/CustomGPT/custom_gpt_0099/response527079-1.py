
from unittest import TestCase
from unittest.mock import patch, MagicMock

def funcToGetBar():
    # This function would normally return some object
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(TestCase):

    @patch('__main__.funcToGetBar')  # Adjust the module's path as necessary
    def testGetBar(self, mock_func):
        # Create a mocked bar object
        mocked_bar = MagicMock()
        expected_return_val = [1, 2, 3]

        # Set the 'some_attr' attribute on the mocked_bar
        mocked_bar.some_attr = expected_return_val
        mock_func.return_value = mocked_bar  # Patch funcToGetBar to return mocked_bar

        # Call the function under test
        result = foo()

        # Assert that the returned value is as expected
        self.assertEqual(expected_return_val, result)

# If running the test
if __name__ == "__main__":
    import unittest
    unittest.main()
