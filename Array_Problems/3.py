import sys
input = sys.stdin.readline

def solve():
    def find_max(arr, idx = 0, maxNum = 0):
        if idx == len(arr):
            return maxNum
        return find_max(arr, idx + 1, max(maxNum, arr[idx]))
    arr = list(map(int, input().split()))
    print(find_max(arr))
if __name__ == "__main__":
    solve()