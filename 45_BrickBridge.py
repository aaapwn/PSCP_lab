"""BrickBridge"""
def main():
    """BrickBridge"""
    aaa = int(input())
    bbb = int(input())
    goal = int(input())
    longg = 5*(bbb)
    if longg > goal:
        longg = 5*(goal//5)
    ans = goal - longg
    if ans > aaa:
        print(-1)
    if ans <= aaa:
        print(ans)
main()
