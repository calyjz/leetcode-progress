class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        needed_count = length = len(p)
        s = list(s)
        p = Counter(p)
        present = defaultdict(int)
        ans = []
        print(p, needed_count)

        for i, char in enumerate(s):

            #process exiting char
            if i >= length:
                exit_char = s[i - length]
                present[exit_char] -= 1

                if exit_char in p and present[exit_char] < p[exit_char]:
                    needed_count += 1

            #process incoming char
            present[char] += 1

            if char in p and present[char] <= p[char]:
                needed_count -= 1

                if needed_count == 0:
                    ans.append(i - length + 1) 



        return ans