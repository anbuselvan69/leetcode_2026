class Solution:
    def majorityFrequencyGroup(self, s):
        a = {}

        for c in s:
            a[c] = a.get(c, 0) + 1

        b = {}

        for c in a:
            f = a[c]
            b[f] = b.get(f, "") + c

        ans = ""
        best = 0

        for f in b:
            if len(b[f]) > len(ans):
                ans = b[f]
                best = f
            elif len(b[f]) == len(ans) and f > best:
                ans = b[f]
                best = f

        return ans