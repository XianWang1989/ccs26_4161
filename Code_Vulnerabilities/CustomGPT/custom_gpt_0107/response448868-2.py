
# Without package
import swap
reload(swap)
swap.printSomething()

# With package
import swapPackage.swap as swap
reload(swap)
swap.printSomething()
