"""Sequence VIII"""
def main():
    """Sequence VIII"""
    num = int(input())
    space = num-1
    for i in range(1, num+1):
        for _ in range(space):
            print("   ", end="")
        for j in range(1, i+1):
            print("%02d " %j, end="")
        print()
        space -= 1
main()
