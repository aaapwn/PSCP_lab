"""Impostor"""
import json
def main():
    """Impostor"""
    player = {}
    died = {}
    alive = {}
    imposter = 0
    while True:
        invite = input()
        if invite == "Start":
            break
        player.update(json.loads(invite))
    while True:
        kill = input()
        if kill == "End":
            break
        died.update({kill:player[kill]})
    for i in player:
        if i not in died:
            alive.update({i:player[i]})
    for j in alive:
        if alive[j] == "Impostor":
            imposter += 1
    print("%d Impostor Remains" %imposter)
    print("***Alive***")
    for k in sorted(alive):
        print("%s : %s" %(k, alive[k]))
    print("***Dead***")
    for lll in sorted(died):
        print("%s : %s" %(lll, died[lll]))
main()
