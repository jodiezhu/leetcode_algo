class Solution(object):
    def min_window(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        # 1.Count the frequencies for chars in t
        hash_map = {}
        for c in t:
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1


        # 2. moving start and end 
        start, end = 0, 0       
        min_window_length = len(s) + 1 # If the minimal length doesn't change, it means there's no valid window        
        min_window_start = 0 # Start point of the minimal window        
        num_of_chars_to_be_included = len(t)

        while end < len(s):
            # If the current char is desired
            if s[end] in hash_map:
                if hash_map[s[end]] > 0:
                    num_of_chars_to_be_included -= 1
                hash_map[s[end]] -= 1

            # If the current window has all the desired chars
            while num_of_chars_to_be_included == 0:
                if end - start + 1 < min_window_length:
                    min_window_length = end - start + 1
                    min_window_start = start

                if s[start] in hash_map:
                    hash_map[s[start]] += 1
                    if hash_map[s[start]] > 0:
                        num_of_chars_to_be_included += 1
                    print(hash_map,num_of_chars_to_be_included)
                start += 1
            end += 1

        if min_window_length == len(s) + 1: #inital large number
            return ""
        else:
            return s[min_window_start:min_window_start + min_window_length]


s=Solution()
print(s.min_window("EBBANC","ABC"))
