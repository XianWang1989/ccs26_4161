
#!/usr/bin/python3

class MyClass(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, MyClass):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)

# Example usage
obj1 = MyClass(1)
obj2 = MyClass(1)
obj3 = MyClass(2)

print(obj1 == obj2)  # True
print(obj1 == obj3)  # False
