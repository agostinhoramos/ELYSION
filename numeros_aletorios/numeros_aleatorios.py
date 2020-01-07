from random import randint

def EscreveTabela(i, t, na):
    print("-" * 30)
    print(i, t, na)

def UmTeste():
    f = [0]*6
    p = [0.0]*6
    for i in range (50):
        x = 1
        na = randint(1 , 6) - 1
        EscreveTabela(i, f, na+1)
        f[na] = f[na] + 1
        EscreveTabela(i, f, na+1)

    for i in range (6):
        p[i] = f[i] /50.0 *100
    for i in range (6):
        print("%5.2f" % p[i])

import date , time
data_hoje = date .now ()
print ( data_hoje )


UmTeste()
     
    
