import sys
input = sys.stdin.readline

def solve():
    def arr_sum(arr, idx = 0, s = 0):
        if idx == len(arr):
            return s
        return arr_sum(arr, idx + 1, s + arr[idx])
    arr = list(map(int, input().split()))
    print(arr_sum(arr))

if __name__ == "__main__":
    solve()