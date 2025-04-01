class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        result=[[1]]
        for i in range(1,numRows):
            prev=result[i-1]
            new=[1]
            for j in range(1,i):
                new.append(prev[j-1]+prev[j])
            new.append(1)
            result.append(new)
        return result