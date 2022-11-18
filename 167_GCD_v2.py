"""GCD_v2"""
def main():
    """GCD_v2"""
    num = [float(input()), float(input())]
    max_num = num[1]
    min_num = num[0]
    if min_num == 0:
        return print(int(max_num))
    while True:
        gcd = max_num%min_num
        if gcd == 0:
            return print(int(min_num))
        else:
            max_num = min_num
            min_num = gcd
main()
