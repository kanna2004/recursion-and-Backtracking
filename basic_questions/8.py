import sys
input = sys.stdin.readline

def solve():
    def count_digits_rec(n):
        if n == 0:
            return 0
        return 1 + count_digits_rec(n // 10)
    n = int(input().strip())
    print(count_digits_rec(n))

if __name__ == "__main__":
    solve()