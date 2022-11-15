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
    if days < 10000:
        print("%04d:%02d:%02d:%02d" %(days, hrs, minn, sec))
    else:
        print("ERR_:__:__:__")
main()
