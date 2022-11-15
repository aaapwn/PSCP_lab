"""CoPrimeV1"""
def main():
    """CoPrimeV1"""
    num = [int(input()), int(input())]
    num.sort()
    if num[0] == 0:
        gcd = num[1]
    for i in range(num[0], 0, -1):
        if num[0]%i == 0 and num[1]%i == 0:
            gcd = i
            break
    if gcd == 1:
        print("YES", gcd, sep="\n")
    else:
        print("NO", gcd, sep="\n")
main()
