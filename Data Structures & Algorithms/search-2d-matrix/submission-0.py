class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)
        while l < r:
            mid = (r + l) // 2

            if matrix[mid][0] > target:
                r = mid
            
            else:
                l = mid + 1
        
        
        row = max(0, l - 1)

        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] == target: return True
            
            if matrix[row][mid] < target: l = mid + 1
            else: r = mid - 1
        
        return False