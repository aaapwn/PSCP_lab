"""ChristmasTree"""
def main():
    """ChristmasTree"""
    nnn = int(input())
    kkk = int(input())
    space = nnn-1
    wood_space = nnn-2
    leaf = 1
    roundd = 1
    while roundd <= nnn:
        print(" "*space, end="")
        print("*"*leaf, end="")
        print(" "*space)
        roundd += 1
        leaf += 2
        space -= 1
    roundd = 1
    while roundd <= kkk:
        print(" "*wood_space, end="")
        print("-"*3, end="")
        print(" "*wood_space)
        roundd += 1
main()
