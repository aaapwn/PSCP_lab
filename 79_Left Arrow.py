"""Left Arrow"""
def main():
    """Left Arrow"""
    kkk = int(input())
    nnn = int(input())
    space = int((nnn-1)/2)
    for i in range(space, -1-space, -1):
        print(" "*abs(i), end="")
        print("*"*kkk)
main()
