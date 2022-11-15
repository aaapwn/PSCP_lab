""" Sequence XI """

def main():
    """ print """
    row = int(input())
    for i in range(-row+1, row):
        for j in range(-row+1, row):
            if abs(i) > abs(j)-1:
                print("%02d" %(row-abs(i)), end=' ')
            else:
                print("%02d" %(row-abs(j)), end=' ')
        print()
main()
