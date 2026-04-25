
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return True  # Implement your equality logic here
        return False

    def __hash__(self):
        return hash(id(self))  # Use an appropriate hash value

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # This will now work without warnings
print(hash(obj1))    # Hash can be called without warnings
