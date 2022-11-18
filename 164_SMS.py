"""SMS"""
def main():
    """SMS"""
    press = {
        "2":["A", "B", "C"],
        "3":["D", "E", "F"],
        "4":["G", "H", "I"],
        "5":["J", "K", "L"],
        "6":["M", "N", "O"],
        "7":["P", "Q", "R", "S"],
        "8":["T", "U", "V"],
        "9":["W", "X", "Y", "Z"]
        }
    ans = ""
    for _ in range(int(input())):
        key = input()
        value = int(input())
        if key == "1":
            for _ in range(value):
                if len(ans) > 0:
                    ans = ans[:-1]
            continue
        while value > len(press[key]):
            value -= len(press[key])
        ans = ans + press[key][value-1]
    if len(ans) == 0:
        print("null")
    else:
        print(ans)
main()
