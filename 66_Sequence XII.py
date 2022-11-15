""" Sequence XII """

def main():
    """ print """
    row = int(input())
    for i in range(-row+1, row):
        for j in range(-row+1, row):
            print("%02d" %(row-abs(abs(i)-abs(j))), end=' ')
        print()
main()
