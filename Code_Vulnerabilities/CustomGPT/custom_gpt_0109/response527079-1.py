
from unittest.mock import MagicMock, patch
import unittest

# This is the function you want to test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test case
class TestFoo(unittest.TestCase):

    @patch('__main__.funcToGetBar')  # Update this path as necessary
    def test_get_bar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_val = ["obj1", "obj2"]

        # Set the attribute directly on the mocked object
        setattr(mocked_bar, "some_attr", expected_return_val)
        mock_func.return_value = mocked_bar  # Set the mock return value

        result = foo()

        self.assertEqual(expected_return_val, result)

# Run tests
if __name__ == '__main__':
    unittest.main()
