"""HorizontalHistogram"""
def sortword(word):
    """sort"""
    if word.isupper():
        return ord(word)+1000
    return ord(word)

def main():
    """HorizontalHistogram"""
    text = input()
    word = set()
    ans = {}
    for i in text:
        word.add(i)
    word = list(word)
    word.sort(key=sortword)
    for j in word:
        ans[j] = ""
    for k in text:
        ans[k] += "-"
        if ans[k].count("-")%5 == 0 and ans[k].count("-") != text.count(k):
            ans[k] += "|"
    for mmm in ans:
        print("%s : %s" %(mmm, ans[mmm]))
main()
