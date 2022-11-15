"""GraderMachine"""
def main():
    """GraderMachine"""
    start = int(input())
    stop = int(input())
    total = 0
    print("pass :", end=" ")
    if start < stop:
        while start <= stop:
            if start % 2 == 0:
                total += start
                print("%d" % start, end=" ")
            start += 1
    else:
        while start >= stop:
            if start % 2 == 0:
                total += start
                print("%d" % start, end=" ")
            start -= 1
    print()
    print("Sum : %d" % total)
main()
