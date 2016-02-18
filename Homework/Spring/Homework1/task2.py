try:
    foo()
except RuntimeError:
    print("Caught RuntimeError")
except AssertionError:
    print("Caught AssertionError")
except MemoryError:
    print("Caught MemoryError")
