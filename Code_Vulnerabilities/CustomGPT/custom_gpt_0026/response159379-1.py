
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
if __name__ == "__main__":
    obj1 = MyClass(10)
    obj2 = MyClass(10)
    obj3 = MyClass(20)

    print(obj1 == obj2)  # True
    print(obj1 == obj3)  # False
