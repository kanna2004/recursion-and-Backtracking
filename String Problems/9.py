import sys
input = sys.stdin.readline

def solve():
    #Print all substrings of a string (recursive)
    def print_substrings(s, idx = 0):
        if idx == len(s):
            return ''
        s[idx] + return print_substrings(s, idx + 1)
        print_substrings(s, idx + 1)
    s = input().strip()
    print(print_substrings(s))


if __name__ == "__main__":
    solve()