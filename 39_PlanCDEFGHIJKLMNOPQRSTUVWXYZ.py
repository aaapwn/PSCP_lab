"""why i cant use sort and list"""
def main():
    """why i cant use sort and list"""
    ans1 = 1
    ans2 = 1
    ans3 = 1
    order = input()
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
    if order == "Descend":
        print("%.2f, %.2f, %.2f" %(ans3, ans2, ans1), sep=", ")
        return
    print("%.2f, %.2f, %.2f" %(ans1, ans2, ans3), sep=", ")
main()
