"""Circular II"""
import math
def main():
    """calculate"""
    xxx1 = float(input())
    yyy1 = float(input())
    rrr1 = float(input())
    xxx2 = float(input())
    yyy2 = float(input())
    rrr2 = float(input())
    dis = math.sqrt(((xxx1-xxx2)**2)+((yyy1-yyy2)**2))
    if rrr1+rrr2 > dis:
        print("Yes")
    else:
        print("No")
main()
