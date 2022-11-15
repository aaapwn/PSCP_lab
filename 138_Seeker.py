"""Seeker"""
def main():
    """Seeker"""
    text = input()+"A"
    ans = 0
    word = ""
    for i in text:
        if i.isnumeric():
            word += i
        else:
            if len(word) > 0 and word.isnumeric():
                ans += int(word)
            word = ""
    print(ans)
main()
