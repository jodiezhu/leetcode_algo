
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        start, end= 0, 0
        count,length = 0, 1
        hash_map = {}

        for end in range(len(s)):
            if s[end] in hash_map:
                hash_map[s[end]]+=1
            else:
                hash_map[s[end]]=1
                count+=1

            while count>2:
                if s[start] in hash_map:
                    hash_map[s[start]]-=1
                    if hash_map[s[start]]==0:
                        count-=1
                        hash_map.pop(s[start])
                start+=1

            length=max(length,end-start+1)

        return length

            
s=Solution()
print(s.lengthOfLongestSubstringTwoDistinct('baecceb'))
