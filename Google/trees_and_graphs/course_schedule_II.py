# Course Schedule II
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