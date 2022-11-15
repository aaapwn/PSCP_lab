"""Quadrant"""
def main():
    """Quadrant"""
    xxx = int(input())
    yyy = int(input())
    if (xxx > 0) and (yyy > 0):
        print("Q1")
    elif (xxx < 0) and (yyy > 0):
        print("Q2")
    elif (xxx < 0) and (yyy < 0):
        print("Q3")
    elif (xxx > 0) and (yyy < 0):
        print("Q4")
    elif (xxx == 0) and (yyy == 0):
        print("O")
    elif (xxx == 0) and (yyy != 0):
        print("Y")
    elif (yyy == 0) and (xxx != 0):
        print("X")
main()
