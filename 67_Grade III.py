"""Grade III"""
def main():
    """Grade III"""
    num = int(input())
    ans = 0
    for _ in range(num):
        xxx = float(input())
        if 95 <= xxx <= 100:
            ans += 4
        elif 90 <= xxx < 95:
            ans += 3.5
        elif 85 <= xxx < 90:
            ans += 3
        elif 80 <= xxx < 85:
            ans += 2.5
        elif 75 <= xxx < 80:
            ans += 2
        elif 70 <= xxx < 75:
            ans += 1.5
        elif 65 <= xxx < 70:
            ans += 1
        elif 60 <= xxx < 65:
            ans += 0.5
        elif 0 <= xxx < 60:
            ans += 0
    ans = ans/num
    print("%.2f" %((int(ans*100))/100))
main()
