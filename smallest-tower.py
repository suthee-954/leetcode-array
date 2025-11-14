
a = [4,8,3,1,5,3,100,3,4,23,1]
b=[-1]*len(a)
print(b)
for i in range (0,len(a)):
    flag = 0
    index=nindex = -1
    data=ndata = -1
    for j in range (0,len(b)):
      if i != j: 
        if(a[j]<a[i]):
            flag=1 
            ndata=a[j]
            nindex=j 
        
        if((flag==1 and index==-1) or (a[index]>a[nindex])) :
            index = nindex
            data = ndata
            b[i]=nindex
            
        if(data == ndata):
            in1 = abs(i-nindex)
            in2 = abs(i-index)
            if(in1>in2):
                b[i]=index
            elif(in1<in2):
                b[i]=nindex
            elif(in1==in2):
                if(index>nindex):
                    b[i]=nindex
                elif(index<nindex):
                    b[i]=index
    
    if(flag==0):
        b[i]=-1
        
print(b)        
        
            
            
            
