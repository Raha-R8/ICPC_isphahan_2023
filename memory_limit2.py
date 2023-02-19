t= int(input())
lst =[]
i = 0
for i in range(t):
    inp = input().split()
    n = inp[0]
    k = inp[1]
    
    if len(n) == int(k):
        print(0)
        
    else:
        while len(set((str(int(n)+i)))) != int(k):
            i+=1
        lst+=[i]
print(*lst, sep = '\n')



