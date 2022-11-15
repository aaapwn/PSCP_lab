"""OneTwo"""
def onetwo(nnn):
    """onetwo"""
    if nnn == 1:
        return "1"
    elif nnn == 2:
        return "2"
    else:
        return onetwo(nnn-1) + onetwo(nnn-2)
print(onetwo(int(input())))
