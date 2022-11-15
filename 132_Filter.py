"""Filter"""
import json
def main():
    """Filter"""
    data = json.loads(input())
    data = dict(sorted(data.items()))
    pan = float(input())
    nub = 0
    for i in data:
        if float(data[i]) >= pan:
            print("%s\t%.2f" %(i, float(data[i])))
            nub += 1
    if nub == 0:
        print("Nope")
main()
