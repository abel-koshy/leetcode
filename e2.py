# Maximum Subarray
arr = [79,-14,25,91,-519,-26,82,-11,11,55,-28,-78,84,49,22,-73,-79,-37,40,12,-7,53,-26,-80,31,-94,51,-97,-98,56,34,-54,-88,-32,-17,-29,17,18,20,32,-49,91,54,-65,40,-47,-39,38,-8,-99,-73,84,30,0,-96,-38,5,32,-36,-16,-35,74,29,-23,-80,-88,47,36,29,-32,-54,79,-64,76,91,53,-71,-71,-9,-3,-93,17,-19,36,94,-38,97,-1,70,-62,82,-65,-87,11,11,-68,-1,-41,44,-71,3,89]
newarr=[]
finalarr=[]
fs=0
ns=0
flag=1
sp=0
cp=0
sum=0
while(sp<len(arr)):
    while (cp<len(arr)):
        newarr.append(arr[cp])                  #adds a new element to the subarray untile th ecp is out of range from starting point onwards
        for i in range(len(newarr)):   #calculate the usm of the subarray
            ns=ns+newarr[i]
        if(ns>fs or flag==1):
            
            print(ns,"updated")
            fs=ns
            finalarr=newarr
        cp=cp+1
        flag = 0
        ns=0
    sp=sp+1
    cp=sp
    newarr=[]
    flag=0
print("ans:",finalarr,fs)