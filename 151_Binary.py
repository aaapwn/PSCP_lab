"""Binary"""
def main():
    """Binary"""
    num = int(input())
    ans = []
    if num == 0:
        return print(0)
    while not num == 0:
        ans.append(num%2)
        num //= 2
    ans.reverse()
    print(*ans, sep="")
main()
