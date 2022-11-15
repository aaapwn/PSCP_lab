"""All_Primes"""
def checkprime(num):
    """checkprime"""
    if num == 1 or num == 0:
        return 0
    for i in range(2, num):
        if num%i == 0:
            return 0
    return 1

def main():
    """All_Primes"""
    num = int(input())
    ans = 0
    for i in range(1, num+1):
        ans += checkprime(i)
    print(ans)
main()
