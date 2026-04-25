
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return True  # or implement your comparison logic
        return False

    def __hash__(self):
        return id(self)  # or implement a suitable hash based on your attributes

# Example usage
a = MyClass()
b = MyClass()
print(a == b)  # Outputs: True
print(hash(a))  # Outputs the hash of object 'a'
