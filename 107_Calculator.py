"""Calculator"""
def main():
    """Calculator"""
    num = int(input())
    ans = 0
    if num == 1:
        print(1)
        return
    for i in range(1, num+1):
        ans += len(str(i))
        ans += 1
    print(ans)
main()
