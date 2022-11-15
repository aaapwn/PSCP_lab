"""lab3-11"""
def main():
    """lab3-11"""
    xxx = float(input())
    if 95 <= xxx <= 100:
        print("A")
    elif 90 <= xxx < 95:
        print("B+")
    elif 85 <= xxx < 90:
        print("B")
    elif 80 <= xxx < 85:
        print("C+")
    elif 75 <= xxx < 80:
        print("C")
    elif 70 <= xxx < 75:
        print("D+")
    elif 65 <= xxx < 70:
        print("D")
    elif 60 <= xxx < 65:
        print("F+")
    elif 0 <= xxx < 60:
        print("F")
    else:
        print("ERR")
main()
