
class Example:
    def method_one(self):
        print("This is method one.")

    def method_two(self):
        self.method_one()
        print("This is method two.")

example = Example()
example.method_two()
