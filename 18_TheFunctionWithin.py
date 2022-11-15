"""TheFunctionWithin"""
def func_f(xxx):
    """func_f"""
    ans = 2*xxx
    return ans

def func_g(xxx):
    """func_g"""
    ans = 3*(xxx**4) - (xxx**3) + 2*(xxx**2) + 10
    return ans

def func_h(xxx, yyy, zzz):
    """func_h"""
    ans = ((zzz + xxx)**2) - xxx*yyy + yyy**2
    return ans

def func_i(aaa, bbb, ccc, ddd):
    """func_i"""
    ans = (aaa**2 + bbb**2 - ccc**2)/(ddd**2 - 2*aaa*ddd + 2*aaa)
    return ans

def calculate():
    """calculate"""
    aaa = float(input())
    bbb = float(input())
    ccc = float(input())
    ddd = float(input())
    print(func_f(func_f(aaa)))
    print(func_g(func_f(aaa - bbb)))
    print(func_h(func_f(aaa+bbb), func_f(aaa+ccc), func_g(func_f(ddd**2))))
    print(func_i(func_h(func_f(aaa+bbb), func_f(aaa-ccc), func_g(func_f(ddd**2))),\
        func_g(func_f(aaa-bbb)), func_f(func_f(func_f(func_f(func_f(ccc))))), ddd**8))
calculate()
