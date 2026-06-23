from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        freq = Counter(nums)

        return heapq.nlargest(k, freq.keys(), key=freq.get)