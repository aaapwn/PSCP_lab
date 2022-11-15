"""WordSequence II"""
def main():
    """WordSequence II"""
    text1 = input()
    text2 = input()
    for i in range(max(len(text1), len(text2)) + 1):
        print(text2[:i] + text1[i:])
main()
