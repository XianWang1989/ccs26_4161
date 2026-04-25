
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        # Check for equality condition
        return False

    def __hash__(self):
        # Return a hash value, ensure consistent behavior with __eq__
        return id(self)  # or use some other logic to generate a hash if needed
