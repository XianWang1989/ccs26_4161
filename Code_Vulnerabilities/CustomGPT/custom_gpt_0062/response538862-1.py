
class Example:
    def method_one(self):
        print("This is method one.")
        self.method_two()

    def method_two(self):
        print("This is method two.")

    def method_three(self):
        print("This is method three.")

# Example usage
example = Example()
example.method_one()
example.method_three()
