import sys
input = sys.stdin.readline

def solve():
    def find_min(arr, idx = 0, minNum = 0):
        if idx == len(arr):
            return minNum
        return find_min(arr, idx + 1, min(minNum, arr[idx]))
    arr = list(map(int, input().split()))
    print(find_min(arr))
if __name__ == "__main__":
    solve()