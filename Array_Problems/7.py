import sys
input = sys.stdin.readline

def solve():
    #Find last occurrence of an element
    # defining a recursive function with four parameteres:
    # i.e, array, index, target element, target element index
    # check index one by one if curr index == target element:
    # then target element index = max(target element index, curr index)
    # for that set target element index = -1
    # in the base case i.e, if we reach the last index we return the target element idex
    def find_last(arr, target_ele, idx = 0, target_ele_idx = -1):
        if idx == len(arr):
            return target_ele_idx
        if arr[idx] == target_ele:
            target_ele_idx = max(idx, target_ele_idx)
        return find_last(arr, target_ele, idx + 1, target_ele_idx)
    arr = list(map(int, input().split()))
    target_ele = int(input())
    print(find_last(arr, target_ele))

if __name__ == "__main__":
    solve()