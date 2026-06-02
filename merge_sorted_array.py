def mergesortedarray(nums1,n,nums2,m):
    p1=n-1
    p2=m-1
    p=n+m-1
    while p1>=0 and p2>=0:
        if nums1[p1]>nums2[p2]:
            nums1[p]=nums1[p1]
            p1-=1
        else:
            nums1[p]=nums2[p2]
            p2-=1
        p-=1
    return nums1
nums1=[1,2,0,0,0]
n=2
nums2=[3,4,5]
m=3
print(mergesortedarray(nums1,n,nums2,m))        
