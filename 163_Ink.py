"""Ink"""
import math
def main():
    """waranthorn"""
    ink = input().split()
    for _ in range(int(ink[1])):
        pos = input().split()
        dis = math.sqrt(float(pos[0])**2 + float(pos[1])**2)
        time = math.ceil(dis/float(ink[0]))
        print(time)
main()
