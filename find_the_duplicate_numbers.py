def duplicatenumber(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
nums=[1,22,22];
print(duplicatenumber(nums))        