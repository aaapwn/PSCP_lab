"""Calculator V2"""
def main():
    """Calculator V2"""
    first = num = ans = int(input())
    if num == 1:
        return print(1)
    for i in range(len(str(num))-1):
        cal = 9*(10**i)
        ans = ans + (cal*(len(str(cal))))
        num -= cal
    ans = ans + (num*len(str(first)))
    print(ans)
main()
