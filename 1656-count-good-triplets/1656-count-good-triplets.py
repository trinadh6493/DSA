class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        co=0
        n=len(arr)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    m=abs(arr[i]-arr[j])
                    na=abs(arr[j] - arr[k])
                    o=abs(arr[i] - arr[k])
                    if m<=a and na<=b and o<=c:
                        co+=1
        return co
                    