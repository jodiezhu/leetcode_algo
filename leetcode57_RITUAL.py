import numpy as np

class Solution(object):

    def addArrayInt(self,array, other):
        if len(array)==0 & len(other)==0 : return None 
        if len(array)==0: return other
        if len(other)==0:return array

        longerArray,shorterArray=[],[]
        carry=0
        ret=[]
        partialResult =[]

        if len(array)>len(other):
            longerArray=array
            shorterArray=other
        else:
            longerArray=other
            shorterArray=array

        for i in range(0,len(shorterArray)):
            multiplier =shorterArray[i]
            
            for multiplicand in longerArray:
                result = multiplicand * multiplier

                if carry!=0:
                    result+=carry
                    carry=0

                if result>=10:
                    carry=result/10
                    result%=10

                partialResult.append(result)

            if carry!=0:
                partialResult.append(carry)
            for j in range(0,i-1):
                partialResult.append(0,0)

            ret=partialResult

        return ret

a=np.array([9,2,3])
b=np.array([3])
s=Solution()
print(s.addArrayInt(a,b))
