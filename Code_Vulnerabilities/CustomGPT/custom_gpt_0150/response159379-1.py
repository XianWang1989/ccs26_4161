
#!/usr/bin/python3

class MyClass:
    def __eq__(self, other):
        return False

    def __hash__(self):
        return 0  # or any constant value, if your class is not intended to be hashable based on its content
