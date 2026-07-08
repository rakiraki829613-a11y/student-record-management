def smallnumber(nums):
    n=len(nums)
    left=0
    right=n-1
    while(left<right):
      mid=(left+right)//2
      if nums[mid]>right:
         left=mid+1

      else:
         right=mid

    return nums[left]
nums=[1,2,3,4,5]
print(smallnumber(nums))