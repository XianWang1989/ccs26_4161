
#!/usr/bin/python3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return True  # or implement your specific equality logic
        return NotImplemented

    def __hash__(self):
        return hash(id(self))  # or some value that makes sense for your class

# Example usage
a = MyClass()
b = MyClass()

print(a == b)  # True based on current implementation
print(hash(a), hash(b))  # Show the hashes
