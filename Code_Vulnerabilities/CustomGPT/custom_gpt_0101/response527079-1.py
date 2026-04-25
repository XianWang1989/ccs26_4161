
from unittest import TestCase
from unittest.mock import patch, MagicMock

def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

class TestFoo(TestCase):
    @patch('module_containing_funcToGetBar.funcToGetBar')
    def test_get_bar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_val = [obj1, obj2]
        mock_func.return_value = mocked_bar

        # Set the return value for some_attr
        mocked_bar.some_attr = expected_return_val

        result = foo()
        self.assertEqual(expected_return_val, result)
