
from unittest.mock import MagicMock, patch
import pytest

# Assume this is your function to test
def foo():
    bar = funcToGetBar()
    return getattr(bar, "some_attr", None)

# Test case
expected_return_val = [obj1, obj2]  # Mocked return value
mocked_bar = MagicMock()
mocked_bar.some_attr = expected_return_val  # Set the attribute directly

@patch('__main__.funcToGetBar', return_value=mocked_bar)
def test_get_bar(mock_func):
    assert expected_return_val == foo()
