"""CaesarV1"""
def main():
    """CaesarV1"""
    chiper = int(input())
    text = input()
    ans = ""
    for i in text:
        if not i.isalpha():
            ans += i
            continue
        chip = ord(i) + chiper
        while (i.islower() and chip < 97) or (i.isupper() and chip < 65):
            chip += 26
        while (i.islower() and chip > 122) or (i.isupper() and chip > 90):
            chip -= 26
        ans += chr(chip)
    print(ans)
main()
