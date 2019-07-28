class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap=[]
        for a,b in points:
            d=a*a+b*b
            heapq.heappush(heap,(-d,a,b)) # -d is for inverse value of data ( pop minimum distance instead of maximum )
            if len(heap)>K: # Keep length of heap in size K
                heapq.heappop(heap)
        return [[b,c] for a,b,c in heap]