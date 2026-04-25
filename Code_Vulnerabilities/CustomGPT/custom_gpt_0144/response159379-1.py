#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        return False

    def __hash__(self):
        return id(self)
