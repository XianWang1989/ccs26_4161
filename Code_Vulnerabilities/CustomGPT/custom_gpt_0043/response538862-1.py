
class SampleClass:
    def method_one(self):
        print("This is method one")

    def method_two(self):
        self.method_one()  # Calling method_one
        print("This is method two")

# Create instance
sample = SampleClass()

# Call methods
sample.method_two()  # This will navigate and call method_one()
