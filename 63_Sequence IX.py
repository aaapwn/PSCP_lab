"""Sequence IX"""
def main():
    """Sequence IX"""
    num = int(input())
    space = num - 1
    for k in range(1, num+1):
        print("   "*space, end="")
        for i in range(1, k+1):
            print("%02d" %i, end=" ")
        for j in range(k-1, 0, -1):
            print("%02d" %j, end=" ")
        print("   "*space, end="")
        print()
        space -= 1
main()
