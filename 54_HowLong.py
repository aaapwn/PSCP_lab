"""HowLong"""
def main():
    """HowLong"""
    text = input()
    num = 0
    for _ in text:
        num += 1 
    if int(text) < 0:
        num -= 1
    print(num)
main()
