
#!/usr/bin/python3

class MyClass(object):
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False

    def __hash__(self):
        # Implement a suitable hash value for your class
        return 0  # Example hash value, modify as needed
