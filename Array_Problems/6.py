import sys
input = sys.stdin.readline

def solve():
    #Find first occurrence of an element
    # defining a recursive function with four parameteres:
    # i.e, array, index, target element, target element index
    # check index one by one if curr index == target element:
    # then target element index = min(target element index, curr index)
    # for that set target element index = float('inf')
    # in the base case i.e, if we reach the last index and
    # still the target element index remains float('inf') then we return -1
    # i.e, the target element is not found else we return the target element index
    def find(arr, target_element,idx = 0, target_element_index = float('inf')):
        if idx == len(arr):
            return -1 if target_element_index == float('inf') else target_element_index
        if arr[idx] == target_element:
            target_element_index = min(target_element_index, idx)
        return find(arr, target_element, idx + 1, target_element_index)
    arr = list(map(int, input().split()))
    target_element = int(input())
    print(find(arr, target_element))

if __name__ == "__main__":
    solve()