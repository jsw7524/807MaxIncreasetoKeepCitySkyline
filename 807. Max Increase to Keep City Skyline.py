class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        sum=0;
        vertical = self.getMax(grid)
        horizon = self.getMax(list(map(list, zip(*grid))))
        for v in range(0,len(vertical)):
            for h in range(0, len(horizon)):
                sum+=(min(vertical[v],horizon[h])-grid[v][h])
        return sum

    def getMax(self, grid):
        listMax = [max(g) for g in grid]
        return listMax

''''''
print("Test1:")
try:
    sln = Solution()
    testData=[[3,0,8,4],
              [2,4,5,7],
              [9,2,6,3],
              [0,3,1,0]]
    result = sln.maxIncreaseKeepingSkyline(testData)
    assert result==35
    print("pass")
except:
    print("failure")

''''''
print("Test2:")
try:
    sln = Solution()
    testData=[[3,0,8,4],
              [2,4,5,7]]
    result = sln.maxIncreaseKeepingSkyline(testData)
    assert result==10
    print("pass")
except:
    print("failure")