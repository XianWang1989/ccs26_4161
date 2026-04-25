
#!/usr/bin/python3

class MyClass(object):
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # or your actual equality logic

    def __hash__(self):
        return hash(id(self))  # or your own hashing logic

# Example usage
a = MyClass()
b = MyClass()

print(a == b)  # Outputs: False
print(hash(a), hash(b))  # Does not raise any warning
