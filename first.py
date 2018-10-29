def f1():
    print("f1 is in first.py")

print("Top level line in first.py")

if __name__ == "__main__":
    print("first.py is run directly")
else:
    print("first.py is imported in another module")