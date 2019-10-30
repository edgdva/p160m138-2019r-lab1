print("Hello, everyone!")
import sys

def greet(name: str):
 return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet(sys.argv[1]))