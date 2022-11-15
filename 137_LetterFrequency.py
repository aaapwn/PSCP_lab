"""LetterFrequency"""
import string
def main():
    """LetterFrequency"""
    text = input().lower().replace(" ", "")
    word = set()
    ans = ""
    nub = float("-inf")
    for k in string.punctuation:
        text = text.replace(k, "")
    for mmm in range(10):
        text = text.replace(str(mmm), "")
    for i in text:
        word.add(i)
    for j in word:
        if text.count(j) >= nub:
            nub = text.count(j)
            ans = j
    print(ans)
main()
