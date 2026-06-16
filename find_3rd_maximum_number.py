def thirdmaximumnumber(nums):
    nums=list(set(nums))
    nums.sort(reverse=True)
    if len(nums)>=3:
        return nums[2]
    return [0]
nums=[1,2,34,58]
print(thirdmaximumnumber(nums))
