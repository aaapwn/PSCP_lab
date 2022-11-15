"""Coke V2"""
def main():
    """Coke V2"""
    price = now_price = int(input())
    lid = int(input())
    sale = int(input())
    want = int(input())
    if lid == 0:
        return print(price*want)
    if price == 0 or want == 0:
        return print(0)
    promoprice = ((want-1)//lid)*sale
    nonpromo = (want-1-((want-1)//lid))*price
    print(now_price+promoprice+nonpromo)
main()
