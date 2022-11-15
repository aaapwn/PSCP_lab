"""B - Fully pair?"""
def main():
    """B - Fully pair?"""
    text = input()
    word = ""
    ans = ""
    for i in text:
        if word.count(i) == 0:
            word += i
    for j in word:
        if int(text.count(j))%2 != 0:
            ans += j
    if len(ans) != 0:
        print(ans)
    else:
        print("fully paired")
main()
