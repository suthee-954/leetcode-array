class Solution:
    def romanToInt(self, s: str) -> int:

        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        array =[]
        result=0
        for i in s:
            if(len(array)==0):
                array.append(roman[i])
            elif(array[-1]>roman[i]):
                result+= array[-1]
                array.pop()
                array.append(roman[i])
            elif(array[-1]<roman[i]):
                val=array[-1]
                val=roman[i]-val
                result+=val
                array.pop()
            elif( array[-1]==roman[i]):
                result+= array[-1]
                array.pop()
                array.append(roman[i])

        if(len(array)!=0):
         
            result+=array[-1]
            array.pop()
                 

        return result
            
                        

        
