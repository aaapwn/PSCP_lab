"""isprime_small"""
def main():
    """isprime_small"""
    num = int(input())
    if num == 1 or num == 0:
        return print("No")
    for i in range(2, num):
        if num%i == 0:
            return print("No")
    print("Yes")
main()
