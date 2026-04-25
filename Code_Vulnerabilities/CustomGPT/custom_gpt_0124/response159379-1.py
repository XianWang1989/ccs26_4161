
#!/usr/bin/python -3

class MyClass(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, MyClass):
            return self.value == other.value
        return NotImplemented

    def __hash__(self):
        return hash(self.value)

# Example usage
a = MyClass(1)
b = MyClass(1)
c = MyClass(2)

print(a == b)  # True
print(a == c)  # False
print(hash(a))  # Hash based on value
print(hash(b))  # Hash based on value
