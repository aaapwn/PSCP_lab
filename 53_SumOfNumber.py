"""SumOfNumber"""
def main():
    """SumOfNumber"""
    num1 = int(input())
    total = 0
    while True:
        num2 = int(input())
        if num2 > 0:
            num2 += 1
        if num2 == num1 or num2 == -1:
            print(total)
            return
main()
