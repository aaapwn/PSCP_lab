"""Flatten"""
import json
def main():
    """Flatten"""
    listt = json.loads((input()))
    ans = []
    def flat(value):
        """flat"""
        for i in value:
            if isinstance(i, (int, float)):
                if isinstance(i, (int, float)):
                    ans.append(i)
            if isinstance(i, list):
                flat(i)
    for i in listt:
        if isinstance(i, (int, float)):
            ans.append(i)
        if isinstance(i, list):
            flat(i)
    print(sorted(ans, reverse=True))
main()

