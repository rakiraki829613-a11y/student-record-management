def duplicateelements(nums):
    k=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[k]=nums[i]
            k+=1
    return k
nums=[1,1,2]
print(duplicateelements(nums))
