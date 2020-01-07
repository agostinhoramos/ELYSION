

def listarTodos():
    f = open("Titulos.csv", "rt", encoding='utf-8')
    titulos = f.readlines()
    f.close()
    # print(titulos)
    for titulo in titulos:
        titulo = titulo.rstrip('\n')
        # v1
        # v = titulo.split(";")
        # print(v[0], v[1], v[2])
        # print("%3s  %-5s  %s" % (v[0], v[1], v[2]))
        # v2
        IDTitulo, CdTitulo, NmTitulo = titulo.split(";")
        print("%3s  %-5s  %s" % (IDTitulo, CdTitulo, NmTitulo))

def pesquisaID():
    IDPesquisar = input("ID do título a pesquisar ?")
    f = open("Titulos.csv", "rt", encoding='utf-8')
    titulos = f.readlines()
    f.close()
    # print(titulos)
    enc = False
    for titulo in titulos:
        titulo = titulo.rstrip('\n')
        IDTitulo, CdTitulo, NmTitulo = titulo.split(";")
        if IDPesquisar == IDTitulo:
            enc = True
            print("%3s  %-5s  %s" % (IDTitulo, CdTitulo, NmTitulo))
    if not enc:
        print("O título com ID %s não existe." % IDPesquisar)


def eliminarTituloPorID(ID):
    f = open("Titulos.csv", "wt", encoding='utf-8')
    titulos = f.readlines()
    f.close()
    for t in titulos:
        t = t.rstrip('\n')
        IDTitulo, CdTitulo, NmTitulo = t.split(";")
        if IDTitulo != ID:
            print(IDTitulo, CdTitulo, NmTitulo, file=f, sep=';')
    f.close()

def alterarTituloPorID(ID, IDTituloNovo, CdTituloNovo, NmTituloNovo):
    f = open("Titulos.csv", "rt", encoding='utf-8')
    titulos = f.readlines()
    f.close()
    f = open("Titulos.csv", "wt", encoding='utf-8')
    for t in titulos:
        t = t.rstrip('\n')
        IDTitulo, CdTitulo, NmTitulo = t.split(";")
        if IDTitulo == ID:
            print(IDTituloNovo, CdTituloNovo, NmTituloNovo, file=f, sep=';')
        else:
            print(IDTitulo, CdTitulo, NmTitulo, file=f, sep=';')
    f.close()


def eliminarID():
    ID = input("ID do título a eliminar ?")
    f = open("Titulos.csv", "rt", encoding='utf-8')
    titulos = f.readlines()
    f.close()
    # print(titulos)
    enc = False
    for titulo in titulos:
        titulo = titulo.rstrip('\n')
        IDTitulo, CdTitulo, NmTitulo = titulo.split(";")
        if ID == IDTitulo:
            enc = True
            print("%3s  %-5s  %s" % (IDTitulo, CdTitulo, NmTitulo))
            conf = input("Eliminar (S/N) ?")
            if conf == 'S':
                eliminarTituloPorID(ID)
                break
    if not enc:
        print("O título com ID %s não existe." % ID)

def alterarID():
    ID = input("ID do título a alterar ?")
    f = open("Titulos.csv", "rt", encoding='utf-8')
    titulos = f.readlines()
    f.close()
    # print(titulos)
    enc = False
    for titulo in titulos:
        titulo = titulo.rstrip('\n')
        IDTitulo, CdTitulo, NmTitulo = titulo.split(";")
        if ID == IDTitulo:
            enc = True
            print("%3s  %-5s  %s" % (IDTitulo, CdTitulo, NmTitulo))
            conf = input("Alterar (S/N) ?")
            if conf == 'S':
                # pedir novos dados
                print("Novos dados")
                IDTitulo = input("ID ?")
                CdTitulo = input("Código ?")
                NmTitulo = input("Nome ?")
                # gravar os novos dados por cima dos dados antigos
                alterarTituloPorID(ID, IDTitulo, CdTitulo, NmTitulo)
                break
    if not enc:
        print("O título com ID %s não existe." % ID)

alterarID()
# eliminarID()
# pesquisaID()
# listarTodos()

# IDTitulo
# CdTitulo
# NmTitulo

# 1;PhD;Doutor
# 2;Mh;Mestre
# 3;E;Especialista
# 4;L;Licenciado
# 5;B;Bacharel
# 6;T;Técnico