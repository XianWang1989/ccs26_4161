
import sys
print("Current Python Path:")
for path in sys.path:
    print(path)

import swap  # Ensure this imports correctly
reload(swap)
swap.printSomething()  # Should print "Hello from swap!"
