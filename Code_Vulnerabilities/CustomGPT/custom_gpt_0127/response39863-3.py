
user = User(email='test@example.com')
try:
    user.put()
    print("User saved successfully.")
except ValueError as e:
    print(e)
