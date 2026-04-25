
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        # Customize equality comparison as needed
        return False

    def __hash__(self):
        # Return a hash value, you can define your own hashing logic
        return hash((self.__class__,))
