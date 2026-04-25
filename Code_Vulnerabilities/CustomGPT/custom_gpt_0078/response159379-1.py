
#!/usr/bin/python3 -3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return True  # Define your equality logic here
        return False

    def __hash__(self):
        return id(self)  # Or use a more appropriate hash value

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # True, according to our equality logic
print(hash(obj1))    # Should not raise warnings now
