
response = postback(1, 'username', None)  # Calls the first case
response = postback(2, 'username', 'some_value')  # Calls the second case
response = postback(3, 'username', 'some_value')  # Calls the third case
response = postback(4, 'username', None)  # Returns None, no action taken
