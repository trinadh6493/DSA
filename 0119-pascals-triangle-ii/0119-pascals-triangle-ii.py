class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        
        result=[[1]]
        for i in range(1,rowIndex+1):
            prev=result[i-1]
            new=[1]
            for j in range(1,i):
                new.append(prev[j-1]+prev[j])
            new.append(1)
            result.append(new)
        return result[rowIndex]
