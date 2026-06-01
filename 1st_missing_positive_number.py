def firstmissingpositivenumber(nums):
    n=len(nums)
    for i in range(n):
        while 1<=nums[i]<=n and nums[i]!=nums[nums[i]-1]:
            corrent_index=nums[i]-1
            nums[i],nums[corrent_index]=nums[corrent_index],nums[i]

    for i in range(n):
        if nums[i]!=i+1:
            return i+1
    return n+1
nums=[1,3,4,5]
print(firstmissingpositivenumber(nums))            