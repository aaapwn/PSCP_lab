"""Run Length Encoding"""
def main():
    """Run Length Encoding"""
    text = input()
    len_text = len(text)
    word = text[0]
    roundd = 0
    for i in range(len_text):
        if text[i] != word:
            print(roundd, word, sep="", end="")
            word = text[i]
            roundd = 1
        elif text[i] == word:
            roundd += 1
    print(roundd, word, sep="")
main()
