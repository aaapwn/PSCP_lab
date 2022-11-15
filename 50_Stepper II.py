"""Stepper II"""
def main():
    """Stepper II"""
    mmm = int(input())
    nnn = int(input())
    if mmm < nnn:
        for i in range(mmm, nnn+1):
            print(i)
    elif mmm > nnn:
        for i in range(mmm, nnn-1, -1):
            print(i)
    elif mmm == nnn:
        print(mmm)
main()
