
print("Current sys.path:")
for path in sys.path:
    print(path)

# Import your modules
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print("ImportError:", e)
