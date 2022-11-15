"""Tuple's Sad life"""
def main():
    """Tuple's Sad life"""
    text = input()
    find = input()
    text = tuple(text.split(" "))
    num = text.index(find)
    height = text.count(find)

    sqare = ((str(num) + " ")*height) + "\n"
    print(sqare*height)
main()
