
import importlib.util
spec = importlib.util.find_spec("SlotMapper")
print(spec)  # Should not return None if it can find the module
