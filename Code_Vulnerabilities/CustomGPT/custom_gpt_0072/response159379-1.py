
#!/usr/bin/python3

class MyClass(object):    
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return True  # or your custom equality logic
        return False

    def __hash__(self):
        return hash(id(self))  # or any suitable hash logic

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # This will call __eq__
print(hash(obj1))  # This will call __hash__
