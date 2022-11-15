"""SaveComputeRepeat"""

def main(start_here):
    """SaveComputeRepeat"""
    millisec = start_here
    sec = millisec//1000
    millisec = millisec%1000
    minn = sec//60
    sec = sec%60
    hrs = minn//60
    minn = minn%60
    days = hrs//24
    hrs = hrs%24
    print('%d %d %d %d %d' %(days, hrs, minn, sec, millisec))
main(492137954293754252786)
