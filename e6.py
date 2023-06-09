class Solution(object):
    def strStr(self, haystack, needle):
        i = 0
        if (len(needle) > len(haystack)):
            return -1
        while (i < len(haystack)):
            if (haystack[i] == needle[0]):
                mat = 1
                if (mat == len(needle)):
                    return (i)
                else:
                    k = 1
                    while (k < len(needle) and i+k < len(haystack)):
                        if (haystack[i+k] == needle[k]):
                            print("k is ", k)
                            mat += 1
                        else:
                            break
                        k += 1
                if (mat == len(needle)):
                    return (i)
            i += 1
        return (-1)
