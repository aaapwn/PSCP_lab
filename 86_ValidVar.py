"""ValidVar"""
def main():
    """ValidVar"""
    num = int(input())
    punctuation = """!\"#%&'()*+,-./:;<=>?@[\\]^`{|}~"""
    reserved = "FalsedefifraiseNonedelreturnTrueelifintryandelseiswhileasexceptlambda\
        withassertfinallynonlocalyieldbreakfornotclassfromorcontinueglobalpass"
    for i in range(num):
        ans = "Valid"
        text = input().strip()
        if text[0].isnumeric() or text in reserved:
            ans = "Invalid"
        for i in text:
            if i in punctuation or i.isspace():
                ans = "Invalid"
        print(ans)
main()
