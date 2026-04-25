from unittest.mock import MagicMock, patch

# The function you are testing
def foo():
    bar = funcToGetBar()
    return bar.getattr("some_attr", None)

# Test setup
mocked_bar = MagicMock()
expected_return_val = [obj1, obj2]  # Replace obj1, obj2 with actual objects or mock objects

# Patch funcToGetBar to return mocked_bar
with patch('__main__.funcToGetBar', return_value=mocked_bar):
    # Mock the `getattr` call on `mocked_bar`
    mocked_bar.getattr.return_value = expected_return_val

    # Run your test
    result = foo()

    # Assert the result is as expected
    assert result == expected_return_val
