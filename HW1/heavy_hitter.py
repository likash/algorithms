from typing import List


def majorityElement(nums: List[int]) -> int:
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
            count += 1
        elif candidate == num:
            count += 1
        else:
            count -= 1

    return candidate


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    result = majorityElement(arr)

    print(result)
