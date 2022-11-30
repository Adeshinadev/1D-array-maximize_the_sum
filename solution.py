test_cases=input()
for i in range(int(test_cases)):
   
    n_k=input().split()
    A=input().split()
    o=int(n_k[1])
    
    g=[]
    for j in range(o):
        
        get_max=max(A)
        r=A.count(get_max)
        g.append(int(get_max)*r)
        z=A.remove(get_max)
        
    print(sum(g))


        



    

