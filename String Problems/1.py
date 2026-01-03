import sys
input = sys.stdin.readline

def solve():
    def print_str(s, idx = 0):
        if idx == len(s):
            return
        print(s[idx])
        print_str(s, idx + 1)
    s = input()
    print_str(s)

if __name__ == "__main__":
    solve()