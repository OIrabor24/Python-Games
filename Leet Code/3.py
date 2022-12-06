def two_sum(nums, target):
    hashmap = {} #val: index 

    for i, n in enumerate(nums):
        diff = target - n 
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[n] = i 
    return 

def groupAnagrams(strs):    
        d={} #sorted string : list of anagrams
        
        # join the '' with sorted word
        for word in strs:
            key = ''.join(sorted(word))
            
        # if word in dict append word to key    
            if key in d:
                d[key].append(word)
        # otherwise d.key equals array word
            else:
                d[key] = [word]
                
        # return values    
        return d.values() 

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs)) 


def logic(strs):
    d={} #sorted string : list of anagrams
        # join the '' with sorted word
    for word in strs:
        key = "".join(sorted(word))
    # if word in dict append word to key    
        if key in d:
            d[key].append(word)
    # otherwise d.key equals array word
        else:
            d[key] = [word]
    # return values    
    return d.values() 

strs = ["eat","tea","tan","ate","nat","bat"]
print(logic(strs)) 