"""key"""
def main():
    """key"""
    num = input()
    key1 = 0
    for i in num:
        key1 += int(i)
    key2 = int(num[-3:])*10
    true_key = key1 + key2
    if true_key < 1000:
        true_key += 1000
    if true_key > 9999:
        true_key = str(true_key)[-4:]
    print(true_key)
main()

