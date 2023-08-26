class Solution:

    def longestKSubstr(self, S, k):
        # code here
        map = {}
        i = -1
        j = -1
        ans = -1
        while True:
            flag1 = False
            flag2 = False
            while i < len(S) - 1:
                flag1 = True
                i += 1
                ch = S[i]
                map[ch] = map.get(ch, 0) + 1
                if len(map) < k:
                    continue
                elif len(map) == k:
                    len_ = i - j
                    ans = max(len_, ans)
                else:
                    break
            while j < i:
                flag2 = True
                j += 1
                ch = S[j]
                if map[ch] == 1:
                    del map[ch]
                else:
                    map[ch] -= 1
                if len(map) == k:
                    len_ = i - j
                    ans = max(ans, len_)
                    break
                elif len(map) > k:
                    continue
            if not flag1 and not flag2:
                break
     
        return ans
