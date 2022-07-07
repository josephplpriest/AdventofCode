def binary_search_row(nums, t):

    if len(nums) == 1:

        if t == nums[0]:
            return True
        else:
            return False

    pivot = len(nums) // 2

    if t >= nums[pivot]:
        return binary_search_row(nums[pivot:], t)
    elif t < nums[pivot]:
        return binary_search_row(nums[:pivot], t)
    else:
        return binary_search_row(nums[pivot], t)


print(binary_search_row([10, 11, 16, 20], 13))
