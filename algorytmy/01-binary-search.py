def binary_search(nums: list[int],  target: int) -> int:
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = nums[mid]

        if guess == target:
            return mid

        if guess < target:
            low = mid + 1
        else:
            high = mid -1

    return None