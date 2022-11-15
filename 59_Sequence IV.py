"""Sequence IV"""
def main():
    """Sequence IV"""
    num = int(input())
    num_output = 1
    for _ in range(num):
        for _ in range(num):
            print("%d " %(num_output), end="")
            num_output += 1
        print()
main()
