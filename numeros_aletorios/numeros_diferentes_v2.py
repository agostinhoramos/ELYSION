V = [1,7,9,7,2,4,9,7,2,8,5,33,77]
N = len(V)
VND=[0]*N
if 1==0:
    V=[0]*N
    for iL in range(N):
        while not ( (V[iL] >= 1) and (V[iL] <= 99) ):
            print ("Números ", "[", iL, "]", " ?")
            V[iL]=int(input())
qnd = 0
for i  in range (N):
# procurar o número de V[i] no vetor
#que tem os números diferentes (VND)
    e = 0
    for j in range (qnd):
        if (V[i] == VND[j]): 
            e = 1
    if (e == 0):  # NÃO ENCONTROU
       # adicionar
        VND[qnd] = V [i] 
        qnd = qnd + 1
          
#Saída de resultados (OUTPUT)
print( "Quantidade de números diferentes: ", qnd)
for i in range(qnd):
    print(VND[i])

