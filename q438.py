


#used sliding windows and hash map

s = "cbaebabacd"
p = "abc"
flist = []
ds={}
dp={}
for i in p:
    if i in dp:
        dp[i]=dp[i]+1
    else:
        dp[i]=1
lp=0
rp=lp+len(p)
for i in s[lp:rp]:              #setting up the dictionary for the first substring of s and we check for this substring lp is valid or not
    if i in ds:
        ds[i]=ds[i]+1
    else:
        ds[i]=1  
    
if(ds==dp):
    print(ds)
    flist.append(lp)

while(rp<len(s)):                                #this loop us responsible fo rth esliding window and we add the next letter in the dictionary for s and then increase rp and then we reduce the left counter in the dictionary then reduce lp. and we then check if th etwo dicitonaryes are the same and if yes lp is appended

    if(s[rp] in ds):
        ds[s[rp]] = ds[s[rp]]+1
    else:
        ds[s[rp]]=1
    rp=rp+1
    ds[s[lp]]=ds[s[lp]]-1
    if (ds[s[lp]]==0):
        del ds[s[lp]]
    lp=lp+1
    if(ds==dp):
        flist.append(lp)
print(flist)
