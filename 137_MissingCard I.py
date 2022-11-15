"""MissingCard I"""
def main():
    """MissingCard I"""
    card = ["A", "K", "J", "Q", 10, 9, 8, 7, 6, 5, 4, 3, 2]
    all_card = []
    for i in card:
        all_card.append(str(i)+"S")
        all_card.append(str(i)+"H")
        all_card.append(str(i)+"D")
        all_card.append(str(i)+"C")
    for _ in range(51):
        getcard = input()
        all_card.remove(getcard)
    print(*all_card)
main()
