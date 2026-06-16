def subarray(nums,k):
    cout=0
    for i in range(len(nums)):
        total=0
        for j in range(i,len(nums)):
             total+=nums[j]
             if total==k:
                 cout+=1
    return cout
nums=[1,1,1,2,2]
k=2
print(subarray(nums,k))