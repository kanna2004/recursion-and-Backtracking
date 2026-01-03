import sys
input = sys.stdin.readline

def solve():
    #Remove all occurrences of a character
    #to remove all occ of a char i.e Target we decalre a recursive func
    # with 4 parameters string s, target char , idx = 0, result string = ''
    # if curr idx or s[idx] == target char then skip the char 
    # else add the s[idx] to res
    # base case if idx == len(s) return result
    def ans(s, target, idx = 0, result = ''):
        if idx == len(s):
            return result
        if s[idx] != target:
            result += s[idx]
        return ans(s, target, idx + 1, result)
    s = input().strip()
    target = input().strip()
    print(ans(s, target))
if __name__ == "__main__":
    solve()