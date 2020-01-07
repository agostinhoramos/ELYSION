
def listarTodos():
    f = open("funcionarios.csv", "rt", encoding='utf-8')
    funcionarios = f.readlines()
    f.close()
    # print(titulos)
    for funcionario in funcionarios:
        funcionario = funcionario.rstrip('\n')
        IDFuncionario,\
        CdFuncionario,\
        CdFuncionario,\
        IDCategoria,\
        IDTitulo,\
        IDServico,\
        IDFuncionarioChefe,\
        EMail,\
        Telemovel,\
        NIF,\
        NCC,\
        DataAdmissao,\
        Vencimento,Vazio,Nome, Apelido = funcionario.split(";")
        print("%3s  %-5s  %s" % (IDFuncionario, CdFuncionario, CdFuncionario))

def contarFuncionariosCategoria():
    idcategoriacontar=input("indica a categoria?");
    f = open("funcionarios.csv", "rt", encoding='utf-8')
    funcionarios = f.readlines()
    f.close()
    n = 0
    for funcionario in funcionarios:
        funcionario = funcionario.rstrip('\n')
        IDFuncionario,\
        CdFuncionario,\
        CdFuncionario,\
        IDCategoria,\
        IDTitulo,\
        IDServico,\
        IDFuncionarioChefe,\
        EMail,\
        Telemovel,\
        NIF,\
        NCC,\
        DataAdmissao,\
        Vencimento,Vazio,Nome, Apelido = funcionario.split(";")
        if idcategoriacontar == IDCategoria:
            n = n + 1
            print("%3s  %-5s  %s" % (IDFuncionario, CdFuncionario, CdFuncionario))
    print ("Total funcionários da categoria  %s: %d" % (idcategoriacontar, n))


def pesquisaFuncionario(ID):
    f = open("funcionarios.csv", "rt", encoding='utf-8')
    funcionarios = f.readlines()
    f.close()
    n = 0
    for funcionario in funcionarios:
        funcionario = funcionario.rstrip('\n')
        v = funcionario.split(";")
        if v[0] == ID:
            return v
    return None

def pesquisaFuncionarioEmail(EmailFuncionario):
    f = open("funcionarios.csv", "rt", encoding='utf-8')
    funcionarios = f.readlines()
    f.close()
    n = 0
    for funcionario in funcionarios:
        funcionario = funcionario.rstrip('\n')
        v = funcionario.split(";")
        # print(v[7])
        if v[7] == EmailFuncionario:
            return v
    return None

def inserirFuncionario():

    while True:
        IDFuncionario = input("IDFuncionario ? ")
        if pesquisaFuncionario(IDFuncionario) == None:
            break
        else:
            print("Funcionário já existe")
    #  nome
    # ...
    while True:
        EmailFuncionario = input("Email ? ")
        if pesquisaFuncionarioEmail(EmailFuncionario) == None:
            break
        else:
            print("Email já existe")

inserirFuncionario()

#inserirFuncionario()

# contarFuncionariosCategoria()
# listarTodos()
