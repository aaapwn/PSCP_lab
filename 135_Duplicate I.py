"""Duplicate I"""
def main():
    """Duplicate I"""
    aaa = set()
    bbb = set()
    mem_a = int(input())
    mem_b = int(input())
    for _ in range(mem_a):
        aaa.add(int(input()))
    for _ in range(mem_b):
        bbb.add(int(input()))
    ans = bbb.intersection(aaa)
    if len(ans) == 0:
        return print("Nope")
    print(*sorted(ans, reverse=True), sep="\n")
main()
