"""One For All"""
def main():
    """One For All"""
    num = int(input())
    ans = ""
    if num != 0:
        for i in range(1, num):
            name = input()
            if i%2 == 1:
                ans = ans + name+("*"*i)
            else:
                ans = ans + name+("-"*i)
        name = input()
        print(ans, end="")
        print("%s_%d" %(name, num))
main()
