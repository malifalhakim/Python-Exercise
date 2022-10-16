'''centered avarage'''

def centered_average(nums):

    nums.sort()

    len_num = len(nums)

    lowest = nums[0]
    highest = nums[-1]

    nums.remove(lowest)
    nums.remove(highest)

    sum = 0

    for num in nums:
        sum += num

    avarage = sum // len_num