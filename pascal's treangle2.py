class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a=[1]
        for i in range(1,rowIndex+1):
            a.append(1)
            for j in range(len(a)-2,0,-1):
                a[j]+=a[j-1]

        return a
