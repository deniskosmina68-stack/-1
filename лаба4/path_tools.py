import os

def show_files():
    print("\nФайли в поточній папці:")
    for name in os.listdir("."):
        print(name)
