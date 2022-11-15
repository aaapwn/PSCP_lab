"""CompositeFunction"""
def func_f(xxx):
    """cal func_f"""
    return 2*xxx

def func_g(xxx):
    """cal func_g"""
    return xxx/2+1

def main():
    """main"""
    xxx = int(input())
    print("%.2f" %(func_f(func_g(xxx))))
    print("%.2f" %(func_g(func_f(xxx))))
main()
