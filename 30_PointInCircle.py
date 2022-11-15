"""PointInCircle"""
def main():
    """PointInCircle"""
    x_1 = float(input())
    y_1 = float(input())
    r_1 = float(input())
    h_1 = float(input())
    k_1 = float(input())
    ans = (((x_1-h_1)**2)+((y_1-k_1)**2))
    if ans <= (r_1**2):
        print("True")
    else:
        print("False")
main()
