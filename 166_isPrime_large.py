"""isPrime_large"""
def main():
    """isPrime_large"""
    num = int(input())
    num_cal = int(num**0.5)+1
    if num == 1 or num == 0:
        return print("NO")
    for i in range(2, num_cal):
        if num%i == 0:
            return print("NO")
    print("YES")
main()
