from typing import List
import heapq

# class Recurse(Exception):
#     def __init__(self, *args, **kwargs):
#         self.args = args
#         self.kwargs = kwargs
#
#
# def recurse(*args, **kwargs):
#     raise Recurse(*args, **kwargs)
#
#
# def tail_recursive(f):
#     def decorated(*args, **kwargs):
#         while True:
#             try:
#                 return f(*args, **kwargs)
#             except Recurse as r:
#                 args = r.args
#                 kwargs = r.kwargs
#                 continue
#     return decorated
#
#
# class Solution:
#     def scheduleCourse(self, not_sorted_courses: List[List[int]]) -> int:
#         courses = sorted(not_sorted_courses, key=lambda x: x[1])
#         n = len(courses)
#
#         @tail_recursive
#         def scheduleCourseRecursive(currentPosition: int,
#                                     currentCourses: List[int],
#                                     solutions: List[List[int]]) -> List[List[int]]:
#
#             print(solutions)
#
#             if currentPosition >= n and len(currentCourses) == 0:
#                 return solutions[:]
#             elif currentPosition >= n:
#                 recurse(currentCourses[-1] + 1, currentCourses[:-1],
#                                                solutions + [currentCourses])
#             elif conflict(currentPosition, currentCourses):
#                 recurse(currentCourses[-1] + 1, currentCourses[:-1], solutions[:])
#             else:
#                 recurse(currentPosition + 1, currentCourses + [currentPosition], solutions[:])
#
#         def conflict(currentPosition: int, currentCourses: List[int]) -> bool:
#             if currentPosition in currentCourses:
#                 return True
#             if currentCourses is None or len(currentCourses) == 0:
#                 return not (courses[currentPosition][0] <= courses[currentPosition][1])
#
#             list_current_courses = [courses[k] for k in currentCourses]
#             return not (sum([i[0] for i in list_current_courses]) + 
#                 courses[currentPosition][0] 
#                 <= courses[currentPosition][1])
#
#         anwser = scheduleCourseRecursive(0, [], [[]])
#         print(anwser)
#         return max([len(i) for i in  anwser])

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])
        A, curr = [], 0
        for dur, ld in courses:
            heapq.heappush(A,-dur)
            curr += dur
            if curr > ld: curr += heapq.heappop(A)
        return len(A)

sol = Solution()
# courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
# courses = [[1,2]]
# courses = [[3,2],[4,3]]
courses = [[914,9927],[333,712],[163,5455],[835,5040],[905,8433],[417,8249],[921,9553],[913,7394],[303,7525],[582,8658],[86,957],[40,9152],[600,6941],[466,5775],[718,8485],[34,3903],[380,9996],[316,7755]]
print(sol.scheduleCourse(courses))
