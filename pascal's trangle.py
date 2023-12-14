class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        pascal = [[1]]
        for i in range(1, numRows):
            prev_row = pascal[i-1]  
            current_row = [1]  
            for j in range(1, i):
                current_row.append(prev_row[j-1] + prev_row[j])
            current_row.append(1)  
            pascal.append(current_row)  
        return pascal
