def removetheoccurence(nums,val):
    k=0
    for i in range(len(nums)):
        nums[i]!=nums[i-1]
        nums[k]=nums[i]
        k+=1
    return k
nums=[1,1,2,3,4]
val=3
ans=(removetheoccurence(nums,val))
print(ans)
print(nums)    