import sys
input = sys.stdin.readline

def solve():
    #Find index of all occurrences of a value
    # we declare a recursive function with 4 parameters
    # the array, target, idx = 0, and a result array which is empty
    # Base case : if idx == len(arr) -> return result array
    # if arr[idx] == target -> result.append(idx)
    # recursive call: return func(arr, target, idx + 1, result)
    def occ_idx(arr, target, idx = 0, result = []):
        if idx == len(arr):
            return result
        if arr[idx] == target:
            result.append(idx)
        return occ_idx(arr, target, idx + 1, result)
    arr = list(map(int, input().split()))
    target = int(input())
    print(occ_idx(arr, target))

if __name__ == "__main__":
    solve()