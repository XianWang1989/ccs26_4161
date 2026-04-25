
try:
    import swap
    reload(swap)
    swap.printSomething()
except AttributeError as e:
    print("Error:", e)
except ImportError as e:
    print("ImportError:", e)
