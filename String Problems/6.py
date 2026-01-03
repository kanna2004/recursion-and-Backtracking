import sys
input = sys.stdin.readline

def solve():
    def construct(s, idx = 0):
        if idx == len(s) - 1:
            return s[idx]
        if s[idx] != s[idx + 1]:
            return s[idx] + construct(s, idx + 1)
        else:
            return construct(s, idx + 1)
    s = input().strip()
    print(construct(s))

if __name__ == "__main__":
    solve()