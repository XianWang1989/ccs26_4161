
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False

    def __hash__(self):
        return 0  # Or any fixed value, or a computed value based on object attributes

# Example usage
a = MyClass()
b = MyClass()

print(a == b)  # Output: False
print(hash(a))  # Output: 0
