V = [12,17,19,17,20,14,19,17,20,18,18,18,18,3,5,6,7,8,3]
N = len(V)
VND=[0]*N
VQND=[0]*N
if 1==0:
    V=[0]*N
    for iL in range(N):
        while not ( (V[iL] >= 1) and (V[iL] <= 99) ):
            print ("Números ", "[", iL, "]", " ?")
            V[iL]=int(input())
qnd = 0
for i  in range (N):
# procurar o número de V[i] no vetorque tem os números diferentes (VND) 
    e = 0; p = 0
    for j in range (qnd):
        if (V[i] == VND[j]): 
            e = 1
            p = j
    if (e == 0):  # NÃO ENCONTROU  # adicionar
        VND[qnd] = V [i]
        VQND[qnd] = 1
        qnd = qnd + 1
    else:
        VQND[p] = VQND[p] + 1
          
#Saída de resultados (OUTPUT)
print (V)
print( "Quantidade de números diferentes: ", qnd)
for i in range(qnd):
    print("%2d %2d " % (VND[i], VQND[i]), end='')
    for j in range(VQND[i]):
        print("*", end='')
    print()    

