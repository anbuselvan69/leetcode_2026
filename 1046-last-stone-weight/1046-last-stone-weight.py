import heapq

class Solution:
    def lastStoneWeight(self, stones):
        heap = []

        for s in stones:
            heapq.heappush(heap, -s)

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            if y != x:
                heapq.heappush(heap, -(y - x))

        if heap:
            return -heap[0]
        return 0
        