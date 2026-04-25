#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        return False

    __hash__ = None  # This makes instances of the class unhashable
