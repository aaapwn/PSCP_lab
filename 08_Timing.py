"""Timing"""
def main():
    '''Timing'''
    sec = int(input())
    minn = sec//60
    sec = sec%60
    hrs = minn//60
    minn = minn%60
    days = hrs//24
    hrs = hrs%24
    print("%d %d %d %d" %(days, hrs, minn, sec))
main()
