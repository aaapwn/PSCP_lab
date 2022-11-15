"""Parity"""
def main():
    """Parity"""
    text = input()
    want = input()
    nub = 0
    for i in text:
        if i == "1":
            nub += 1
    if nub%2 == 0:
        if want == "Odd":
            text += "1"
        else:
            text += "0"
    else:
        if want == "Odd":
            text += "0"
        else:
            text += "1"
    print(text)
main()
