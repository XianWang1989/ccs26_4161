
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return False  # or your actual equality logic here
        return NotImplemented

    def __hash__(self):
        return 0  # or your actual hashing logic here

# Example usage
a = MyClass()
b = MyClass()
print(a == b)  # Outputs: False
