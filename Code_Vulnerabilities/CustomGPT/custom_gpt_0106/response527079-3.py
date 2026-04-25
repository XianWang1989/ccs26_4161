
class TestFoo(unittest.TestCase):
    @patch('__main__.funcToGetBar')  # Adjust the import path as necessary
    def test_get_bar(self, mock_func):
        mocked_bar = MagicMock()
        expected_return_value = ['obj1', 'obj2']

        # Set the expected return value for the attribute
        mocked_bar.some_attr = expected_return_value

        mock_func.return_value = mocked_bar  # Patch funcToGetBar

        result = foo()

        self.assertEqual(expected_return_value, result)

if __name__ == '__main__':
    unittest.main()
