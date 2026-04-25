
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return True  # or your custom equality logic

    def __hash__(self):
        return id(self)  # or your custom hash logic

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # This will now work without warnings
print(hash(obj1))    # This will also work
