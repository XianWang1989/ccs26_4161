
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return True  # or your actual comparison logic
        return False

    def __hash__(self):
        return id(self)  # or your actual hash logic

# Example usage
a = MyClass()
b = MyClass()

print(a == b)  # Should invoke __eq__ and return True
