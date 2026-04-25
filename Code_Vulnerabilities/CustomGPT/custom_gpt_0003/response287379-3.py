
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")
    print("Current sys.path:")
    print(sys.path)
