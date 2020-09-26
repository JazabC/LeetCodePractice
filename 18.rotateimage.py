class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        
        
        for row in range(rows):
            for col in range(row, cols):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
                
        for i in range(rows):
            matrix[i].reverse()
                
        