"""Meteorite"""
def main():
    """Meteorite"""
    weight = float(input())
    breakk = int(input())
    save = float(input())
    meteor = 1
    rocket = 0
    while weight >= save:
        rocket += meteor
        meteor *= breakk
        weight /= breakk
    print(rocket)
main()
