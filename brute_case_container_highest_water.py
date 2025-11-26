class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mult = 0
        newmult=0
        vol = 0 
        newvol = 0
        for i in range(0,len(heights)):
            for j in range(0,len(heights)):
                if i != j:

                    if heights[i]!=heights[j]:
                        s = min(heights[i],heights[j])
                    else:
                        s=heights[i]

                    mul = s
                    vol = abs(i-j)*mul

                if newvol<vol:
                    newmult=mul
                    newvol=vol
        return newvol            
                      



                    
        
