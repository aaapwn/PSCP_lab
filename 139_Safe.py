"""Safe"""
def main():
    """Safe"""
    text1 = input().upper()
    text2 = input().upper()
    ans = 0
    for i, j in zip(text1, text2):
        first = abs(ord(i) - ord(j))
        second = (ord("Z") - ord(i) + 1) + (ord(j) - ord("A"))
        third = (ord(i) - ord("A") + 1) + (ord("Z") - ord(j))
        choose = sorted([first, second, third])
        ans += choose[0]
    print(ans)
main()
