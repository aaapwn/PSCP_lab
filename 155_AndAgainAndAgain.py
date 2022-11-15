"""AndAgainAndAgain"""
import string
def main():
    """AndAgainAndAgain"""
    text = input()
    nub = 0
    sara = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in string.punctuation:
        text = text.replace(i, "")
    word = sorted(text.split(" "))
    for j in word:
        countsara = 0
        for k in sara:
            countsara += j.count(k)
        if countsara > 1:
            print(j)
            nub += 1
    if nub == 0:
        print("Nope")
main()
