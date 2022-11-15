"""Boomerang"""
import math
def function1(xxx):
    """calculate function1"""
    ans1 = xxx+1
    print(ans1)
def function2(yyy):
    """calculate function2"""
    ans2 = (7*(yyy**3))+(2*(yyy**2))-(31*yyy)+1
    print(ans2)
def function4(xxx, yyy):
    """calculate function4"""
    ans3 = (xxx+yyy)*(xxx-yyy)
    print(ans3)
def function5(xxx, yyy, zzz):
    """calculate fucntion5"""
    ans4 = (yyy-(math.sqrt((yyy**2)-(4*xxx*zzz))))/(2*xxx)
    print(ans4)

def main():
    """Boomerang"""
    xxx = int(input())
    yyy = int(input())
    zzz = int(input())
    function1(xxx)
    function2(yyy)
    print(-zzz)
    function4(xxx, yyy)
    function5(xxx, yyy, zzz)
main()

