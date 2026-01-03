import sys
input = sys.stdin.readline

def solve():
    def check_sorted(arr, idx = 0):
        if idx == len(arr):
            return True
        if arr[idx] > arr[idx + 1]:
            return False
        return check_sorted(arr, idx + 1)
    arr = list(map(int, input().split()))
    print(check_sorted(arr))

if __name__ == "__main__":
    solve()