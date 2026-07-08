def consugative(nums):
    num_set=set(nums)
    longest=0
    for num in num_set:
        if num-1 not in num_set:
            leangth=1
            while num+1 in num_set:
                leangth+=1
        longest=max(longest,leangth)
    return longest 
nums=[100,2,3,4,5]
print(consugative(nums))          