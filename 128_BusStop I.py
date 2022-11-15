"""BusStop I"""
def main():
    """BusStop I"""
    capacity = int(input())
    inbus = []
    pai = int(input())
    ans = 0
    for i in range(1, pai+1):
        text = input()
        people = text.split()
        people.pop(0)
        while str(i) in inbus:
            inbus.remove(str(i))
            ans += 1
        for j in people:
            if int(j) > i and len(inbus) < capacity:
                inbus.append(j)
    print(ans)
main()
