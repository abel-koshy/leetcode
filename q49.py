strs = ["ddddddddddg", "dgggggggggg"]
from collections import *
dictlet = defaultdict(list)
for i in strs:
    count = [0]*26
    for k in i:
        count[ord(k)-ord("a")] +=1
    print(count)
    dictlet[tuple(count)].append(i)
print(dictlet.values())
