#14. longest common prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        newarr = []
        prefix = ''
        ml = len(strs[0])

        for i in strs:
            if (len(i) < ml):
                ml = len(i)

        for j in range(ml):  # loop deciding how many times to go through words i.e. the lowest length of the prefix or smallest word
                    for i in strs:  # loop for adding the rpefixes
                        newarr.append(i[j])
                    char = newarr[0]
                    for i in strs:
                        if (char in newarr):
                            newarr.remove(char)  # resetting the newarr
                    if(len(newarr) > 0):
                            if(j == 0):
                                return ("")
                            else:
                                return (prefix)
                    prefix = prefix+char

        return (prefix)
