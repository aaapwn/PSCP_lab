"""LargestNumber"""
def compare(val1, val2):
    """Compare number"""
    if val1 > val2:
        return val1
    return val2

def main():
    """Main function"""
    x_val = input()
    y_val = input()
    z_val = input()

    lastest = x_val + y_val + z_val
    lastest = compare((x_val + z_val + y_val), lastest)
    lastest = compare((y_val + x_val + z_val), lastest)
    lastest = compare((y_val + z_val + x_val), lastest)
    lastest = compare((z_val + y_val + x_val), lastest)
    lastest = compare((z_val + x_val + y_val), lastest)
    print(int(lastest))
main()
