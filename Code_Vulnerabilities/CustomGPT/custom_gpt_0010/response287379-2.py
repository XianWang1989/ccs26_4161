
import importlib.util

spec = importlib.util.find_spec("SlotMapper")
print(spec)  # Should not be None if the module is found
