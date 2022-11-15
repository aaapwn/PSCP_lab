"""Ball"""
def main():
    """Ball"""
    height = float(input())
    ans = 0
    while height > 0.01:
        height *= 0.6
        ans += 1
    if ans > 0:
        ans -= 1
    print(ans)
main()
