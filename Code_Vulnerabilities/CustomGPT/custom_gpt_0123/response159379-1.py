
#!/usr/bin/python3

class MyClass(object):    
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return True  # or your actual equality logic
        return False

    def __hash__(self):
        return hash(id(self))  # or an appropriate hash value

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # Should return True
print(hash(obj1))    # Will work without warnings
