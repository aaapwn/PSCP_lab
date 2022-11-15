"""RockPaperScissor"""
def main():
    """RockPaperScissor"""
    text = input()
    aaa = 0
    bbb = 0
    lenn = len(text)
    for i in range(0, lenn, 2):
        if text[i]+text[i+1] == "RP":
            bbb += 1
        if text[i]+text[i+1] == "RS":
            aaa += 1
        if text[i]+text[i+1] == "PR":
            aaa += 1
        if text[i]+text[i+1] == "PS":
            bbb += 1
        if text[i]+text[i+1] == "SR":
            bbb += 1
        if text[i]+text[i+1] == "SP":
            aaa += 1
    if aaa > bbb:
        print("A win %d-%d" %(aaa, bbb))
    if bbb > aaa:
        print("B win %d-%d" %(bbb, aaa))
    if aaa == bbb:
        print("DRAW %d" %aaa)
main()
