"""3nPlus1"""
def main():
    """3nPlus1"""
    while True:
        num = int(input())
        if num == 0:
            return
        ans = 1
        while not num == 1:
            if num%2 == 0:
                num /= 2
            else:
                num = num*3 + 1
            ans += 1
        print(ans)
main()
