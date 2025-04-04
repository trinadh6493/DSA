class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        d={'2':'abc','3':'def','4':{'g','h','i'},'5':{'j','k','l'},'6':{'m','n','o'},'7':{'p','q','r','s'},'8':{'t','u','v'},'9':{'w','x','y','z'}}
        
        l1=[]
        def dfs(dig, com):
            
            if len(dig)==0:
                l1.append(com)
                
            else:
                print("dig is",dig[0],d[dig[0]])
                for i in d[dig[0]]:
                    dfs(dig[1:],com+i)
        dfs(digits,"")
        return l1