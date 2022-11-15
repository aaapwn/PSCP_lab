"""Cat Parade"""
def main():
    """Cat Parade"""
    alll = []
    while True:
        text = input()
        if text == "END":
            break
        if text == "IT'S A DOG":
            alll.pop(len(alll)-1)
            continue
        splitt = text.split(", ")
        for i in splitt:
            alll.append(i)
    listt = list(set(alll))
    # print(listt)
    # print(alll)
    listt.sort()
    for j in listt:
        print(j, alll.index(j)+1, alll.count(j))
main()
