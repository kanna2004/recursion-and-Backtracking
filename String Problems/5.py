import sys
input = sys.stdin.readline

def solve():
    #Replace a character with another
    #we declare a recursive func with 5 parameters
    # string s, target char , replace char and idx, result = ''
    # if s[idx] == trget char -> result += s[:idx] + replace char + s[idx + 1: ]
    # base case -> if idx == len(s) return result
    def construct(s, target, replace, idx = 0, result = ''):
        if idx == len(s):
            return result
        if s[idx] == target:
            result += replace
        else:
            result += s[idx]
        return construct(s, target, replace, idx + 1, result)
    s = input().strip()
    target = input().strip()
    replace = input().strip()
    print(construct(s, target, replace))


if __name__ == "__main__":
    solve()