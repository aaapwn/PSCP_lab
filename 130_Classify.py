"""Classify"""
def main():
    """Classify"""
    student = []
    done = []
    while  True:
        stu = input()
        if stu == "END":
            break
        student.append(stu[:4])
    student.sort()
    for i in sorted(list(set(student))):
        if i[:2] not in done:
            print("%d %d %d" %(int(i[:2]), int(i[2:4]), student.count(i)))
            done.append(i[:2])
        else:
            print("-- %d %d" %(int(i[2:4]), student.count(i)))
main()
