# find the largest sum possible from a subarray
arr=[1,2,-2,33,4,5-66,3,34]
newarr=[]
finalarr=[]
fs=0
ns=0
sp=0
cp=0

sum=0
while(sp<len(arr)):
    while (cp<len(arr)):
        newarr.append(arr[cp])                  #adds a new element to the subarray untile th ecp is out of range from starting point onwards
        for i in range(len(newarr)):   #calculate the usm of the subarray
            ns=ns+newarr[i]
        print(newarr,ns)
        if(ns>fs):
            print("updated")
            fs=ns
            finalarr=newarr
        cp=cp+1
        ns=0
    sp=sp+1
    cp=sp
    newarr=[]
print(finalarr,fs)    
        
        
    