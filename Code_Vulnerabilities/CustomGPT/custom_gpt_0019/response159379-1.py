
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False

    def __hash__(self):
        return id(self)  # or any other hash logic

# Example usage
a = MyClass()
b = MyClass()

print(a == b)  # False
print(hash(a) == hash(b))  # Depending on your __hash__ implementation
