
import sys
import maya.standalone
maya.standalone.initialize(name='python')

import swapPackage.swap as swap
import importlib
importlib.reload(swap)
swap.printSomething()
