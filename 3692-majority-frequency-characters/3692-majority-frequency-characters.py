from collections import Counter

class Solution:
    def majorityFrequencyGroup(self, s):
        a = Counter(s)

        b = {}

        for c in a:
            f = a[c]
            b[f] = b.get(f, "") + c

        ans = ""
        best = 0

        for f in b:
            if len(b[f]) > len(ans) or (len(b[f]) == len(ans) and f > best):
                ans = b[f]
                best = f

        return ans