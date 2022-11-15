"""WeightStation"""
def main():
    """WeightStation"""
    avg = float(input())
    lor1 = float(input())
    lor2 = float(input())
    lor3 = float(input())
    lor4 = (avg*4)-(lor1+lor2+lor3)
    if avg*4 > 15000:
        print("Overweight")
        return
    if (lor1 < avg-(avg/2)) or (lor1 > avg+(avg/2)):
        print("Unbalance")
        return
    if (lor2 < avg-(avg/2)) or (lor2 > avg+(avg/2)):
        print("Unbalance")
        return
    if (lor3 < avg-(avg/2)) or (lor3 > avg+(avg/2)):
        print("Unbalance")
        return
    if (lor4 < avg-(avg/2)) or (lor4 > avg+(avg/2)):
        print("Unbalance")
        return
    print("Pass %.2f" %lor4)
main()
