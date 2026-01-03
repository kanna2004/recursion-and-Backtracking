import sys
input = sys.stdin.readline

def solve():
    # Check if a string is palindrome
    # we decalre a recursive function with 3 parameters
    # i.e, the string, left and right pointers
    # Base Case if l >= r we return True as left crosses right
    # if s[l] != s[r] -> return False
    # recursive Call -> func(s, l + 1, r - 1)
    def check(s, l, r):
        if l >= r:
            return True
        if s[l] != s[r]:
            return False
        return check(s, l + 1, r - 1)
    s = input().strip()
    print(check(s, 0, len(s) - 1))

if __name__ == "__main__":
    solve()