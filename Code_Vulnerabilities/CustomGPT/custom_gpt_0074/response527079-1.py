
from unittest.mock import MagicMock, patch

def funcToGetBar():
    # This would normally return a bar object
    pass

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)


class TestFoo:
    @patch('__main__.funcToGetBar')
    def testGetBar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_value = ["obj1", "obj2"]
        mocked_bar.some_attr = expected_return_value  # Set the attribute directly

        mock_func.return_value = mocked_bar  # Patch the function to return the mocked bar

        # Run the test
        result = foo()
        assert result == expected_return_value  # Use the assert function appropriate for your framework

# Example of running the test
if __name__ == "__main__":
    test_instance = TestFoo()
    test_instance.testGetBar()
    print("Test passed!")
