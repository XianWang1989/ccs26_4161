
# Example API simulation
class MockAPI:
    def PostDirectMessage(self, user, message):
        print(f"Sending to {user}: {message}")

def postmarket(user, tval):
    print(f"Handling post market for {user} with value {tval}")

api = MockAPI()

# Example calls
postback(1, 'Alice', 'some_value')
postback(2, 'Bob', 'some_value')
postback(3, 'Charlie', 'some_value')
postback(4, 'David', 'some_value')  # This won't do anything
