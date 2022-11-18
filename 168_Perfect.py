"""Perfect"""
def main():
    """Perfect"""
    num = int(input())
    ans = -1
    for i in range(1, num+1):
        summ = 1
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                summ = summ + j + i/j
        if summ == i:
            ans += i
    print(ans)
main()
