"""Day2011"""
def main():
    """Day2011"""
    month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    day = 0
    now_day = int(input())
    now_month = int(input())
    for i in range(now_month):
        day += month_day[i]
    day += now_day
    day %= 7
    if day == 1:
        print("Saturday")
    if day == 2:
        print("Sunday")
    if day == 3:
        print("Monday")
    if day == 4:
        print("Tuesday")
    if day == 5:
        print("Wednesday")
    if day == 6:
        print("Thursday")
    if day == 0:
        print("Friday")
main()
