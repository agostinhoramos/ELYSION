# Clubes
#   - Inserir
#   - Alterar
#   - Eliminar
#   - Pesquisa por nome
#   - Pesquisa por número de sócios
#
# Atributos:
#   - Sigla: texto 5
#   - Nome: texto 50
#   - Data_Fundacao: Data
#   - Nome_Estadio: texto 50
#   - Nome_Presidente: texto 50
#   - Nome_Treinador: texto 50
#   - Numero_Socios: inteiro
nome_ficheiro_clubes = "Clubes.txt.csv"
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

def LerNome(msg):
    while True:
        Nome = input(msg)
        if ValidaNome(Nome):
            break

def Inserir():
    while True:
        Sigla = input("Sigla?")
        #if Sigla[0:0] >= 'A' and Sigla[0:0] <= 'Z'
        if ValidaSigla (Sigla) == True:
            break
    Nome = LerNome("Nome clube?")
    Data_Fundacao   = input("Data fundação?")
    Nome_Estadio    = LerNome("Nome estádio?")
    Nome_Presidente = LerNome("Nome presidente?")
    Nome_Treinador  = LerNome("Nome treinador?")
    Numero_Socios   = int(input("Número de socios?"))
    f = open(nome_ficheiro_clubes, "at")
    print(Sigla, Nome, Data_Fundacao, Nome_Estadio, Nome_Presidente,
        Nome_Treinador, Numero_Socios, sep=';', file=f)
    f.close()
    # Ler dados
    # Abrir ficheiro em modo adicionar
    # Gravar dados
    # Fechar ficheiro

def MenuGestaoClubes():
    while True:
        print("Gestão de Clubes\n")
        opcoes = ['Inserir',   # print("1 - Inserir")# print("2 - Alterar")
                  'Alterar',
                  'Eliminar',
                  'Pesquisa por sigla',
                  'Presquisa por nome',
                  'Pesquisa por número sócios (intervalo)',
                  'Terminar']
        o = 1
        for opcao in opcoes:
            print("%d - %s" % (o, opcao)); o = o + 1
        op = input("?")
        if op ==  str(len(opcoes)):
            break;
        elif op == '1':
            Inserir()
MenuGestaoClubes()



 # for (i=0; i< 6; i++)   // C
        #     opcoes[i]
        # for i in range(len(opcoes)):
        #     print(opcoes[i])
