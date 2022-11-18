"""SceneSwitch I"""
def main():
    """SceneSwitch I"""
    warm_light = False
    before_second = input()
    turn_on = True
    ans = 0
    if before_second == "End":
        return print(0)
    before_second = float(before_second)
    while True:
        get_second = input()
        if get_second == "End":
            return print(ans)
        get_second = float(get_second)
        if turn_on:
            turn_on = False
            before_second = get_second
            continue
        turn_on = True
        if get_second - before_second <= 6:
            if warm_light:
                warm_light = False
            else:
                warm_light = True
        if get_second - before_second > 6:
            warm_light = False
        if turn_on and warm_light:
            ans += 1
main()
