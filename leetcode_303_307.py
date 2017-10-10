def getsum(BITTree,i):
    s = 0  
    i = i+1 # index in BITree[] is 1 more than the index in arr[]

    while i > 0:
        s += BITTree[i]
        i -= i & (-i)
    return s
 

def updatebit(BITTree , n , i ,v):
    i += 1     # index in BITree[] is 1 more than the index in arr[] 
    while i <= n:      
        BITTree[i] += v # Add 'val' to current node of BI Tree       
        i += i & (-i) # Update index to that of parent: parent[i]=i+i&(-i)
        print(BITTree)
        
def construct(arr, n): 
    BITTree = [0]*(n+1)
 
    for i in range(n):
        updatebit(BITTree, n, i, arr[i])
    # Uncomment below lines to see contents of BITree[]
    #for i in range(1,n+1):
    #      print BITTree[i],
    return BITTree


freq = [1,3,5]
BITTree = construct(freq,len(freq))

freq[1] -= 1
updatebit(BITTree, len(freq),1 , -1) 
print("Sum of elements in arr[0..5] is " + str(getsum(BITTree,2)))
