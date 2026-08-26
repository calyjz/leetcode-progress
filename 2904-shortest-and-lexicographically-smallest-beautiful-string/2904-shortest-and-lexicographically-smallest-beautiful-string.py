class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        if s.count("1") < k:
            return ""

        ans = s
        left = count = 0

        for right, char in enumerate(s):
            count += int(char)

            while count > k or s[left] == "0":
                count -= int(s[left])
                left += 1
            
            if count == k:
                if (right - left + 1) < len(ans):
                    ans = s[left:right + 1]
                elif (right - left + 1) == len(ans) and s[left:right + 1] < ans:
                    ans = s[left:right + 1]
        
        return ans

