import sys  # importiname nuskaitymo biblioteka


def greet(name: str):  # funkcija is uzduoties
    return f"Hello, {name}!"  # vis dar ji


if __name__ == "__main__":  # perduodame i argumenta kintamaji
    print(greet(sys.argv[1]))  # jeigu [0], tai hello.py, jeigu 1, tai tas kas po hello.py