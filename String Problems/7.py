import sys
input = sys.stdin.readline

def solve():
    #Move all 'x' characters to the end
    #Base case: if given string s == '' or len(s) <= -> return s
    # recursive calls:
    # if s[idx] != 'x' -> s[idx] + func(s, idx)
    # else fuc(s, idx) + s[idx]
    def construct(s, idx = 0):
        if idx == len(s):
            return ''
        if s[idx] != 'x':
            return s[idx] + construct(s, idx + 1)
        else:
            return construct(s, idx + 1) + s[idx]
    s = input().strip()
    print(construct(s))


if __name__ == "__main__":
    solve()