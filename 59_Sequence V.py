"""Sequence V"""
def main():
    """Sequence V"""
    num = int(input())
    roundd = 0
    while num > 0:
        print("%d " %num, end="")
        num -= 1
        roundd += 1
        if roundd == 7:
            print()
            roundd = 1
main()


