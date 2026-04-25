
print("Current sys.path:", sys.path)
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")
