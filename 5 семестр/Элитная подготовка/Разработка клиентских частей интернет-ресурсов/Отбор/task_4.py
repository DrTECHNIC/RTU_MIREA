def solution(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return True

def print_result(s: str, t: str):
    print(f"""
Input: s = \"{s}\", t = \"{t}\"
Output: {"true" if solution(s, t) else "false"}""")

def main():
    print_result("anagram", "nagaram")
    print_result("rat", "car")

if __name__ == '__main__':
    main()