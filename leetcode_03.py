class Solution(object):
    def lengthOfLongestSubstring(self,s):
        chars = {}
        pointer, max_len=0,0
        
        for index,value in enumerate(s):
            if value in chars:
                pointer=max(chars[value]+1,pointer)
            max_len=max(max_len,index-pointer+1)
            chars[value]=index
        return max_len
    
s=Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
