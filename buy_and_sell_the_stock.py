def duplicates(nums):
    st=set()     
    for num in nums:
        if num in st:
            return True
        st.add(num)
    return False
nums={1,2,1,21,2}
print(duplicates(nums))