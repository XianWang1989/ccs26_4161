
# Example user and tval values
user = "user123"
tval = "smantana"

# Call with different cases
postback(1, user, tval)  # Calls the first lambda
postback(2, user, tval)  # Calls the second lambda
postback(3, user, tval)  # Calls the third lambda
postback(4, user, tval)  # Does nothing (default case)
