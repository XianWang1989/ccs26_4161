
from unittest.mock import MagicMock, patch

# Assuming this is the function you want to test
def funcToGetBar():
    pass  # This will be mocked in the test

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Your test
class TestFoo:
    @patch('__main__.funcToGetBar')  # Adjust the module path as needed
    def testGetBar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_val = ['obj1', 'obj2']  # Sample expected return value

        # Directly set the attribute on the mock
        mocked_bar.some_attr = expected_return_val
        mock_func.return_value = mocked_bar  # Mock funcToGetBar to return the mocked bar

        # Call the function and assert the result
        assert foo() == expected_return_val

# Example usage of the test class (normally you would use a test runner)
if __name__ == "__main__":
    test = TestFoo()
    test.testGetBar()
