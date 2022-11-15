"""Coke"""
def main():
    """Coke"""
    price = now_price = int(input())
    lid = int(input())
    sale = int(input())
    want = int(input())
    if lid == 0:
        return print(price*want)
    if price == 0 or want == 0:
        return print(0)
    for i in range(1, want):
        if i%lid == 0:
            now_price += sale
            continue
        now_price += price
    print(now_price)
main()
