"""GCD_v1"""
def main():
    """GCD_v1"""
    num = [int(input()), int(input())]
    num.sort()
    if num[0] == 0:
        return print(num[1])
    for i in range(num[0], 0, -1):
        if num[0]%i == 0 and num[1]%i == 0:
            return print(i)
main()
