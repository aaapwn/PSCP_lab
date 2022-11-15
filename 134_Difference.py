"""Difference"""
def main():
    """Difference"""
    aaa = set()
    bbb = set()
    mem_a = int(input())
    mem_b = int(input())
    for _ in range(mem_a):
        aaa.add(int(input()))
    for _ in range(mem_b):
        bbb.add(int(input()))
    ans = aaa - bbb
    print(*sorted(ans))
main()
