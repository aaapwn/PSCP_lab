"""Olympic"""
def main():
    """Olympic"""
    countries = int(input())
    score = {}
    ranking = 1
    nub = 0
    before = [-1, -1, -1]
    for _ in range(countries):
        point = input().split(" ")
        medal = point[1:]
        total = int(point[1])+int(point[2])+int(point[3])
        medal.append(total)
        score[point[0]] = medal
    score = dict(sorted(score.items()))
    score = dict(sorted(score.items(), key=lambda a: int(a[1][2]), reverse=True))
    score = dict(sorted(score.items(), key=lambda a: int(a[1][1]), reverse=True))
    score = dict(sorted(score.items(), key=lambda a: int(a[1][0]), reverse=True))
    for i in score:
        if ranking > 1 and score[i][:3] == before:
            print(nub, i, *score[i])
            ranking += 1
            before = score[i][:3]
            continue
        print(ranking, i, *score[i])
        before = score[i][:3]
        nub = ranking
        ranking += 1
main()
