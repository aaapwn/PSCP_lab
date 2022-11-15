"""Sequence"""
def main():
    """Sequence"""
    num = int(input())
    for i in range(2, num+2):
        num_output = i
        for _ in range(num):
            print("%d " %(num_output), end="")
            num_output += 1
        print()
main()
