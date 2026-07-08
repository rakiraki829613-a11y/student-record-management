def rotate(nums,k):
    n=len(nums)
    k=k%n
    nums[:]=nums[n-k:]+nums[:n-k]
    return nums
nums=[1,2,3,4,5]
k=3
print(rotate(nums,k))
