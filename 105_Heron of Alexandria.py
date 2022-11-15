"""Heron of Alexandria"""
import math
def main():
    """Heron of Alexandria"""
    aaa = float(input())
    bbb = float(input())
    ccc = float(input())
    sss = (aaa+bbb+ccc)/2
    area = math.sqrt(sss*(sss-aaa)*(sss-bbb)*(sss-ccc))
    print("%.3f" %area)
main()
