def sum67(nums):
    sum = 0

    index_7 = nums.index(7)
    i = 0
    while i < len(nums):
        if nums[i] == 6:
            i = index_7 + 1
        else :
            sum += nums[i]
            i += 1

    return sum