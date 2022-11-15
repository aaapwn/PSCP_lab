"""MAC"""
def main():
    """MAC"""
    text = input()
    check = text.upper()
    base16 = "1234567890ABCDEF.-:"
    if not (len(text) == 17 or len(text) == 14):
        print("ERROR")
        return
    for i in check:
        if i not in base16:
            print("ERROR")
            return
    if not (text.count("-") == 5 or text.count(":") == 5 or text.count(".") == 2):
        return print("ERROR")
    if (text == text[:2]+":"+text[3:5]+":"+text[6:8]+":"+text[9:11]\
        +":"+text[12:14]+":"+text[15:]) and ("." not in text) and ("-" not in text):
        print("VALID 2")
    elif text == (text[:2]+"-"+text[3:5]+"-"+text[6:8]+"-"+text[9:11]\
        +"-"+text[12:14]+"-"+text[15:]) and (":" not in text) and ("." not in text):
        print("VALID 1")
    elif text == (text[:4]+"."+text[5:9]+"."+text[10:]) and (":" not in text) and ("-" not in text):
        print("VALID 3")
    else:
        print("ERROR")
main()
