"""FOR!F-Ball"""
def main():
    """FOR!F-Ball"""
    g_l = 1
    g_c = 0
    g_r = 0
    text = input()
    for i in text:
        if i == "A":
            n_gl = g_c
            g_c = g_l
            g_l = n_gl
        elif i == "B":
            n_gc = g_r
            g_r = g_c
            g_c = n_gc
        elif i == "C":
            n_gl = g_r
            g_r = g_l
            g_l = n_gl
    if g_l == 1:
        print(1)
    if g_c == 1:
        print(2)
    if g_r == 1:
        print(3)
main()
