import sys
input = sys.stdin.readline

def solve():
    # Find max ele in an unsorted array using divide and conquer
    # we declare a recursive function with 3 parameters:
    # arr, low, high
    # Base case if low == high i.e, only one element -> return arr[low]
    # mid = low + high // 2
    # lef call -> func(arr, l, mid)
    # right call -> func(arr, mid + 1, r)
    # return max(leftcall, right call)
    def find_max(arr, l, h):
        if l == h:
            return arr[l]
        mid = (l + h) // 2
        left_max = find_max(arr, l, mid)
        right_max = find_max(arr, mid + 1, h)
        return max(left_max, right_max)
    arr = list(map(int, input().split()))
    print(find_max(arr, 0, len(arr) - 1))

if __name__ == "__main__":
    solve()