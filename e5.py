# #26. Remove Duplicates from Sorted Array
# non decreasing: 11234
# increasing order: 12345

nums=[]
lp = 1
for rp in range(1,len(nums)):
    if (nums[rp] != nums[rp-1]):
        nums[lp] = nums[rp]
        lp += 1
        rp += 1
    
        
print (lp)

