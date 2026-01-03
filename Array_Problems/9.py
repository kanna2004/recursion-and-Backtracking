import sys
input = sys.stdin.readline

def solve():
    #Print array in reverse order
    # We decalre a recursive func with 2 parameters
    # size of the input arr and the input arr
    # base case if size reaches 0 we print the ele and return out
    '''def print_rev(n, arr):
        if n == 0:
            print(arr[n])
            return
        print(arr[n - 1])
        return print_rev(n - 1, arr)'''
    def print_rev(idx, arr):
        if idx < 0:
            return
        print(arr[idx])
        print_rev(idx - 1, arr)
    n = int(input())
    arr = list(map(int, input().split()))
    print(print_rev(n, arr))

if __name__ == "__main__":
    solve()