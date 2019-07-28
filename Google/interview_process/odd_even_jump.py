class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        l = len(A)
        odd_jump = [-1]*l #odd_jump[i], when odd jump from index i, what index it is going to land
        even_jump = [-1]*l #even_jump[i], when even jump from index i, what index it is going to land

        odd = [False]*l #odd[i], can index i, starting by odd jump, go to the end
        even = [False]*l #even[i], can index i, starting by even jump, go to the end
        odd[-1] = True
        even[-1] = True

        #construct odd_jump
        stack = []
        for n, i in sorted((n, i) for i, n in enumerate(A)):
        	while stack and stack[-1]<i:
        		odd_jump[stack.pop()] = i
        	stack.append(i)

        #construct even_jump
        stack = []
        for n, i in sorted((-n, i) for i, n in enumerate(A)):
        	while stack and stack[-1]<i:
        		even_jump[stack.pop()] = i
        	stack.append(i)

        for i in reversed(range(l-1)):
        	if odd_jump[i]!=-1:
	        	odd[i] = even[odd_jump[i]]
	        if even_jump[i]!=-1:
	        	even[i] = odd[even_jump[i]]

        return sum(odd)