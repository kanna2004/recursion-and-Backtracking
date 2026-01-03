import sys
input = sys.stdin.readline

def solve():
    #Count vowels in a string
    #we make set(vowels) and check if curr idx in vowels count ++
    def count_vowels(s, idx = 0, count = 0, vowels = set('aeiou')):
        if idx == len(s):
            return count
        if s[idx] in vowels:
            count += 1
        return count_vowels(s, idx + 1, count, vowels)
    s = input().strip()
    print(count_vowels(s))


if __name__ == "__main__":
    solve()