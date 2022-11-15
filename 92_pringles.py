"""Pringles"""
def main():
    """Pringles"""
    line1 = input()
    first_inbox = input()
    line2 = input()
    longg = int(input())
    num = len(first_inbox)-1
    pickable = first_inbox[:longg].count(")")
    if longg >= num:
        last_inbox = (" "*num)+"|"
    else:
        last_inbox = (" "*longg)+first_inbox[longg:]
    print(pickable)
    if last_inbox.count(")") == 0:
        print("None.")
    else:
        print("There are still some left.")
    print(line1)
    print(last_inbox)
    print(line2)
main()
