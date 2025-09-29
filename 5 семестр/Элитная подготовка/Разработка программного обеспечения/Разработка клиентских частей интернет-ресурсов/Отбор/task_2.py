def solution(nums1: list, m: int, nums2: list, n: int):
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

def print_result(nums1: list, m: int, nums2: list, n: int):
    nums1_copy: list = nums1.copy()
    solution(nums1_copy, m, nums2, n)
    print(f"""
Input: nums1 = {nums1}, m = {m}, nums2 = {nums2}, n = {n}
Output: {nums1_copy}""")

def main():
    print_result([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    print_result([1], 1, [], 0)
    print_result([0], 0, [1], 1)

if __name__ == '__main__':
    main()