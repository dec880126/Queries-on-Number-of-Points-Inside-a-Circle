# Leetcode  ->  Medium
# Queries on Number of Points Inside a Circle
# Input: points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
# Output: [3,2,2]
# Explanation: The points and circles are shown above.
# queries[0] is the green circle, queries[1] is the red circle, and queries[2] is the blue circle.

# Original complement: Runtime =  2880 ms ; Memory =  14.5 MB
class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        count = [0] * len(queries)
        for q in range(len(queries)):
            c_x = queries[q][0]
            c_y = queries[q][1]
            for p in range(len(points)):
                p_x = points[p][0]
                p_y = points[p][1]
                length = (p_x-c_x) ** 2 + (p_y-c_y) ** 2
                if length <= queries[q][2] ** 2:
                    count[q] += 1
        return count
        
#Paramater
points = [[1,1],[2,2],[3,3],[4,4],[5,5]]
queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]

#Main Function
def main():
    output = Solution()
    print(output.countPoints(points, queries))

if __name__ =='__main__':
    main()