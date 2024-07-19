flag=[268, 413 ,438 ,313 ,426 ,337 ,272 ,188 ,392 ,338 ,77 ,332 ,139 ,113 ,92 ,239 ,247 ,120 ,419 ,72,295,190,131]
result=[]

for i in range(len(flag)):
    start=1
    while 1:
        d=(flag[i]*start)%41
        if d==1:break
        start+=1
    result.append(start)

for i in range(len(result)):
    if result[i]<27:
        print(chr(result[i]+ord('a')-1),end="")
    elif result[i]==37:
        print("_",end="")
    else:
        print(result[i]-27,end="")    
    
    
    
