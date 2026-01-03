import sys
input = sys.stdin.readline

def solve():
    #Count occurrences of an element
    # we decalre a recursive function to find the occ
    # with 4 parameters i.e, arr, target, idx, count
    # if arr[idx] == target we increase count by 1
    # Base case  if idx == len(arr) we return count
    def count_occ(arr, target, idx = 0, count = 0):
        if idx == len(arr):
            return count
        if arr[idx] == target:
            count += 1
        return count_occ(arr, target, idx + 1, count)
    arr = list(map(int, input().split()))
    target = int(input())
    print(count_occ(arr, target))

if __name__ == "__main__":
    solve()