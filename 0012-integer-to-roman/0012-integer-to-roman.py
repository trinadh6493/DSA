class Solution:
    def intToRoman(self, num: int) -> str:
        numb=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        rom=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

        n=num
        i=0
        s=""
        while n>0:
            print(n,s)
            if n>=numb[i]:
                s+=rom[i]
                n-=numb[i]
            else:
                i+=1
        return s