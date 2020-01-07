def ValidaNome(nome):
    import re
    regex = r"[A-Z][a-z]{2,8}( [a-z]{2,3}){0,1}( [A-Z][a-z]{2,8}){1,4}"
    matches = re.finditer(regex, nome, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False

def ValidaSigla(sigla):
    import re
    regex = r"[A-Z]{3,5}"
    matches = re.finditer(regex, sigla, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False


def LerNumeroInteiro0(msg, min, max):
    while True:
        n = int(input(msg))
        if n >= min and n <= max:
            break
        else:
            print ("O valor deve estar entre %d e %d" % (min, max))

def LerNumeroInteiro1(msg, min, max):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print ("Não digitou um número inteiro!")
            continue
        if n >= min and n <= max:
            break
        else:
            print ("O valor deve estar entre %d e %d" % (min, max))

# ns = LerNumeroInteiro1("Número sócio?", 0, 100)

def LerNumero(msg, min, max, tipo="inteiro",):
    # tipo in ["inteiro", "real"]
    while True:
        try:
            if tipo=="inteiro":
                n = int(input(msg))
            else:
                n = float(input(msg))
        except ValueError:
            print ("Não digitou um número inteiro!")
            continue
        if n >= min and n <= max:
            break
        else:
            print ("O valor deve estar entre %d e %d" % (min, max))
# ni = LerNumero("Número sócio?", 0, 100)
# print(type(ni))
# ni = LerNumero("Número sócio?", 0, 100, "inteiro")
# print(type(ni))
# nr = LerNumero("Número sócio?", 0, 100, "real")
# print(type(nr))
# exit();


def LerData(msg, min=None, max=None):
    from datetime import datetime
    while True:
        data_texto = input(msg)
        try:
            data = datetime.strptime(data_texto, '%Y-%m-%d')
        except ValueError:
            print("Data inválida")
            continue
        if data >= min and data <= max:
            break;
        else:
            print("Data fora do intervalo %s e %s"
                  % (min.strftime ("%Y-%m-%d"),
                     max.strftime ("%Y-%m-%d")))

from datetime import datetime
data_min = datetime.strptime("2018-01-01", '%Y-%m-%d')
data_max = datetime.strptime("2018-12-31", '%Y-%m-%d')
data_fundacao = LerData("Data fundação?", data_min, data_max)




agora = datetime.now()
print (agora)
print ("Data: ", agora.strftime ("%Y-%m-%d"))
print ("Hora: ", agora.strftime ("%X"))


