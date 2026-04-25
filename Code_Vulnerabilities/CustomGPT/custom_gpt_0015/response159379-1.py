
#!/usr/bin/python -3

class MyClass(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

# Example usage
a = MyClass(10)
b = MyClass(10)
c = MyClass(20)

print(a == b)  # True
print(a == c)  # False
print(hash(a) == hash(b))  # True
