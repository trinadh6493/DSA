class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n=len(s)
        if numRows<2 or n<3:
            return s
        list_of_lists = [[] for _ in range(numRows)]
        k=0
        print("N IS ",n)

        def funct1(k):
            i=0
            while i<numRows and k+i<n:
                #print(s[k+i])
                print("k is ",k,"row no ",i,"alphabet ",s[k+i])
                list_of_lists[i].append(s[k+i])
                i+=1
            #print("k value here is",k+i)
            if k+i<n:
                #print("k value here is",k+i)
                print("k after funct1 is ",k+i)
                funct2(k+i)
        def funct2(k):
            i=0
            #print("k is ",k)
            print("k+i in 2 is ",k+i,"numRows-i-2 is",numRows-i-1)
            while i<numRows-1 and k+i<n and numRows-i-2>0:
                #print(s[k+i])
                print("k is ",k,"row no ",numRows-i-2,"alphabet ",s[k+i])
                list_of_lists[numRows-i-2].append(s[k+i])
                i+=1
            print("reached here")
            if k+i<n:
                print("k value after funct2 is",k+i-1)
                funct1(k+i)
        funct1(k)
        print(list_of_lists)
        s1=""
        for i in range(len(list_of_lists)):
            my_string = "".join(list_of_lists[i])
            s1+=my_string
        return s1