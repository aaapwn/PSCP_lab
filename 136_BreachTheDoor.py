"""BreachTheDoor"""
import string
def main():
    """BreachTheDoor"""
    text = input()
    for i in string.punctuation:
        text = text.replace(i, "")
    for mmm in range(10):
        text = text.replace(str(mmm), "")
    text = text.split(" ")
    for j in text:
        if len(j) > 6:
            print(j, end=" ")
main()
