def mmissingnumber(nums):
    i=0
    n=len(nums)
    while n>i:
        correct=nums[i]
        if nums[i]<n and nums[i]!=nums[correct]:
            nums[i],nums[correct]=nums[correct],nums[i]

        else:
            i+=1
    for i in range(n):
        if nums[i]!=i:
            return i
    return n
nums=[0,1,3,4]
print(mmissingnumber(nums))            