"""ClockHands"""
def main():
    """ClockHands"""
    gethour = int(input())
    getmin = int(input())
    short = ((getmin/60)*5)+(gethour*5)
    # angle = (abs(getmin-short))*6
    # print(angle)
    if getmin <= short < getmin+1:
        print("True")
    else:
        print("False")
main()
