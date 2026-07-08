def majorityelements(nums):
    cout=0
    candidate=0
    for num in nums:
        if cout==0:
            candidate=num
        if candidate==num:
            cout+=1
        else:
            cout-=1
    return candidate
nums=[1,1,1,1,3,3,2,2,2,2,2,2,2,2,5,6,0]
print(majorityelements(nums))               
