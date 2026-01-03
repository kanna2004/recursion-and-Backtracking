import sys
input = sys.stdin.readline

def solve():
    def rev(n, new = 0):
        if n == 0:
            return new
        else:
            return rev(n // 10, new * 10 + n % 10)
    n = int(input().strip())
    print(rev(n))
        

if __name__ == "__main__":
    solve()