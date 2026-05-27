def twosum(nums,target):
    mp={}
    for i in range(len(nums)):
        needed=target-nums[i]
        if needed in mp:
            return [mp[needed],i]
        mp[nums[i]]=i
        nums =[2,3,4,5]
        target=8
        print(twosum(nums,target))