
print( ParseBooRgx("[A-Z]{1,10}", input("R: ")) )



def ParseBooRgx(padrao, valor) :
    import re
    try:
        re.search(padrao, valor)
        return 1
    except:
        return 0