flag=[165 ,248 ,94 ,346 ,299 ,73 ,198 ,221 ,313 ,137, 205 ,87 ,336 ,110 ,186 ,69 ,223 ,213 ,216 ,216 ,177 ,138 ]
result=[]

for i in range(len(flag)):
   result.append(flag[i]%37)

for i in range(len(result)):
    if result[i]<26:
        print(chr(result[i]+ord('A')),end="")
    elif result[i]==36:
        print("_",end="")
    else:
        print(result[i]-26,end="")    
    
    
    
