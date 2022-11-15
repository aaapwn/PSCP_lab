"""Century"""
import math
def main():
    """Century"""
    num = int(input())
    for _ in range(num):
        year = input()
        if "B.E." in year:
            year = int(year[5:])-543
        else:
            year = int(year[5:])
        if year > 0:
            print(math.ceil(year/100))
        else:
            print("ERROR")
main()
