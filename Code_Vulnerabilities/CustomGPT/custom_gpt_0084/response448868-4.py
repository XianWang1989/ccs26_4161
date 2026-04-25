
try:
    import swapPackage.swap as swap
    reload(swap)  # Reload if changes are made
    swap.printSomething()
except AttributeError as e:
    print("An error occurred:", e)
