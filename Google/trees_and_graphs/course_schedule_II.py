# Course Schedule II

"""
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .


[[1,0],[2,0],[3,1],[3,2]]
prereqs = {
    1: [], 
    2: [], 
    3: []
}
1, 2, 3, 4
*

visited = {1, 0, 2 }

course = 2
new_course = 0
path = {}

result = [0, 1, 2, 3]
"""
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        result = []
        free_course = []
        visited = set()
        prereqs = defaultdict(list)
        for reqs in prerequisites:
            prereqs[reqs[0]].append(reqs[1])

        def top_sort(course, path):
            while prereqs[course]:
                new_course = prereqs[course].pop()
                if new_course in path:
                    top_sort.is_cycle = True
                if new_course not in visited:
                    visited.add(new_course)
                    path.add(new_course)
                    top_sort(new_course, path)
            result.append(course)
            path.remove(course)
        top_sort.is_cycle = False
        for i in range(numCourses):
            if i in prereqs and prereqs[i]:
                visited.add(i)
                top_sort(i, set([i]))
                if top_sort.is_cycle:
                    return []
        for i in range(numCourses):
            if i not in prereqs and i not in visited:
                free_course.append(i)
        return free_course + result