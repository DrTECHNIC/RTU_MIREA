def solution(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

def print_result(s: str):
    print(f"""
Input: s = \"{s}\"
Output: {"true" if solution(s) else "false"}""")

def main():
    print_result("()")
    print_result("()[]{}")
    print_result("(]")
    print_result("([])")
    print_result("([)]")

if __name__ == '__main__':
    main()