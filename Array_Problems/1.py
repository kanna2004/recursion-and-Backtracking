import sys
input = sys.stdin.readline

def solve():
    def print_ele(arr, idx = 0):
        if idx == len(arr):
            return
        print(arr[idx])
        print_ele(arr, idx + 1)
    arr = list(map(int, input().split()))
    print_ele(arr)

if __name__ == "__main__":
    solve()