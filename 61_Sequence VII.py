"""Sequence VII"""
def main():
    """Sequence VII"""
    num = int(input())
    roundd = 1
    while roundd <= num:
        for i in range(1, roundd+1):
            print("%d " %i, end="")
        print()
        roundd += 1
    roundd -= 1
    while roundd > 1:
        roundd -= 1
        for i in range(1, roundd+1):
            print("%d " %i, end="")
        print()
main()
