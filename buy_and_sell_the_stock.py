def productself(nums):
    n=len(nums)
    answer=[1]*n
    prifix=1
    for i in range(n):
        answer[i]=prifix
        prifix*=nums[i]

    sufix=1
    for i in range(n-1,-1,-1):
        answer[i]=sufix
        sufix*=nums[i]
    return answer
nums=[1,2,3,4]
print(productself(nums))