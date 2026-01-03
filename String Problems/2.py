import sys
input = sys.stdin.readline

def solve():
    def rev_str(s, idx, result = ''):
        if idx < 0:
            return result
        result += s[idx]
        return rev_str(s, idx - 1, result)
    s = input()
    print(rev_str(s, len(s) - 1))

if __name__ == "__main__":
    solve()