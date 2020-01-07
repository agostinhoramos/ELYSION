from random import randint
fg = [0]*6
for j in range(30):
    #print(randint(1 , 6))
    f = [0]*6
    p = [0.0]*6
    for i in range (50):
        na = randint(1 , 6) - 1
        f[na] = f[na] + 1
        fg[na] = f[na] + 1        
    for i in range (6):
        p[i] = f[i] /50.0 *100
    for i in range (6):
        print("%5.2f" % p[i])
print("-" * 30)
for i in range (6):
     p[i] = fg[i] /50.0 *100
for i in range (6):
     print("%5.2f" % p[i])        
        
        
    
