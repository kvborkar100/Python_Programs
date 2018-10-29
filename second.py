import first

print("top level line in second.py")
first.f1()

if __name__ == "__main__":
    print("Second.py is directly called")
else:
    print("Second.py is imported in another module")
