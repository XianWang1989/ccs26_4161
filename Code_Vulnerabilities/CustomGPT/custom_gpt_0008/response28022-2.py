
user = "example_user"
tval = "some sour cream"

# Call with different cases
postback(1, user, tval)  # Should send the first message
postback(2, user, tval)  # Should call postmarket function
postback(3, user, tval)  # Should send the third message
