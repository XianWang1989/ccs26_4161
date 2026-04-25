
from unittest import TestCase
from unittest.mock import MagicMock, patch

def funcToGetBar():
    # This would be your actual function implementation.
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(TestCase):
    @patch('__main__.funcToGetBar')  # Adjust the path as necessary
    def testGetBar(self, mocked_funcToGetBar):
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Replace with your expected objects
        mocked_bar.some_attr = expected_return_val  # Set the attribute directly
        mocked_funcToGetBar.return_value = mocked_bar

        result = foo()
        self.assertEqual(result, expected_return_val)

# Run the test
if __name__ == "__main__":
    import unittest
    unittest.main()
