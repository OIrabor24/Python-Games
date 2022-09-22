strs = ["flower","flow","flight"]

def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    matching = min(strs,key=len) 

    for i, ch in enumerate(matching):
        for other in strs:
            if other[i] != ch:
                return matching[:i]
    return matching 

