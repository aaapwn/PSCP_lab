"""Shorten"""
def main():
    """Shorten"""
    num = int(input())
    before_num = num
    first_num = str(num)
    nums = str(num)
    ans = ""
    if num != -1:
        while True:
            num = int(input())
            if num-before_num == 1:
                nums = nums + str(num)
            else:
                if len(nums) > 1 and first_num != str(before_num):
                    ans = ans + first_num + "-" + str(before_num)
                    if num != -1:
                        ans += ", "
                else:
                    ans = ans + (nums)
                    if num != -1:
                        ans += ", "
                nums = str(num)
                first_num = str(num)
            if num == -1:
                return print(ans)
            before_num = num
main()
