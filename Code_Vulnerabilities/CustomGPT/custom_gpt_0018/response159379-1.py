
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
    a = MyClass(10)
    b = MyClass(10)
    c = MyClass(20)

    print(a == b)  # True, since values are the same.
    print(a == c)  # False, different values.
    print(hash(a) == hash(b))  # True, since the hash is based on the same value.
