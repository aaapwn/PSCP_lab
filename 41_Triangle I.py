"""triangle"""
def main():
    """why i cant use sort wa bro"""
    ans1 = 1
    ans2 = 1
    ans3 = 1
    var1 = float(input())
    var2 = float(input())
    if var1 > var2:
        ans1 = var2
        ans2 = var1
    else:
        ans1 = var1
        ans2 = var2
    var3 = float(input())
    if var3 < ans1:
        ans3 = ans2
        ans2 = ans1
        ans1 = var3
    elif var3 > ans2:
        ans3 = var3
    else:
        ans3 = ans2
        ans2 = var3
    long = (ans1**2 + ans2**2)**0.5
    if abs(long - ans3) <= 0.01:
        print("Yes")
    else:
        print("No")
main()
