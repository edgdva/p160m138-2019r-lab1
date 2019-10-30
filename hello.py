import sys


<<<<<<< HEAD
def greet(greeted_name: str, shout_count: int = 1):
    return f"Hello, {greeted_name}{shout_count * '!'}"


if __name__ == "__main__":
    n = int(sys.argv[2]) if len(sys.argv) == 3 else 1
    print(greet(sys.argv[1], n))
=======
def greet(greeted_name: str):  # funkcija is uzduoties
    return f"Hello, {greeted_name}!"  # vis dar ji


if __name__ == "__main__":  # perduodame i argumenta kintamaji
    print(greet(sys.argv[1]))  # jeigu [0], tai hello.py, jeigu 1, tai tas kas po hello.py
>>>>>>> master
