import re

from Fn import isValid
from Fn import inFile
from Fn import Algrthm

class GF:

    def Inserir(_url_ = 'Dados/Funcionarios.csv'):
        
        while True:
            IDF = input("IDFuncionário? ")
            RSLT = isValid.IDF(IDF, _url_)
            if RSLT == 'True' :
                break
            else:
                if RSLT == '-1':
                    print('>>> Código inválido! [de 1 até 8 digitos], valor maior que zero o inicio. <<<\n')
                elif RSLT == '-2':
                    print('>>> Já existe Funcionário com este número! <<<\n')
                continue
        
        CDF = Algrthm.CDF(_url_) #Gerado Automaticamente!

        while True:
            NAME = input("Nome Completo do Funcionário? ")
            if re.search("^[A-Z][a-zA-Z]{3,}(?: [A-Z][a-zA-Z]*){0,4}$", NAME ) :
                break
            else:
                print(">>> Nome inválido!, [2-5] Palavras <<<\n")
                continue
        
        while True:
            IDC = input("ID Categoria? ")
            if True:
                break
            else:
                continue

        while True:
            IDT = input("ID Título? ")
            if True:
                break
            else:
                continue

        while True:
            IDS = input("ID Serviço? ")
            if True:
                break
            else:
                continue

        while True:
            IDFC = input("ID Funcionário chefe? ")
            if True:
                break
            else:
                continue

        while True :
            Email = input("Email? ")
            if re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", Email) :
                break
            else:
                print(">>> Este email não é válido! <<<\n")
                continue

        while True:
            Telemovel = input("Telemóvel? ")
            if re.search( "(9[1236]\d{7})+$", Telemovel) :
                break
            else:
                print(">>> Telemóvel não é válido, Prefixo 91, 92, 93, 96! <<<\n")
                continue

        while True:
            NIF = input("NIF? ")
            RSLT = isValid.NIF(NIF)
            if RSLT == 'True' :
                break
            else:
                if RSLT == '-1':
                    print('>>> Apenas inteiros, 8 caracteres! <<<\n')
                elif RSLT == '-2':
                    print('>>> NIF inválido! <<<\n')

                continue
            
        while True:
            NCC = input("NCC [00000000 0 AA0]? ")
            RSLT = isValid.NCC(NCC)
            if RSLT == 'True':
                break
            else:
                if RSLT == '-1':
                    print(">>> Formato inválido!, [eg. 18170480 3 ZZ8] <<<\n")
                elif RSLT == '-2':
                    print('>>> NCC inválido! <<<\n')
                continue

        while True :
            DataAdmissao = input("Data Admissão [YYYY MM DD hh mm ss]? ")
            RSLT = isValid.DATE(DataAdmissao)
            if RSLT == 'True':
                break
            else:
                if RSLT == '-1':
                    print('>>> Formato inválido! [YYYY MM DD hh mm ss] <<<\n')
                elif RSLT == '-2':
                    print('>>> Insira menor ou igual a actual! <<<\n')
                continue

        while True:
            Vencimento = input("Vencimento? ")
            if re.search("([0-9])\d{,7}\.([0-9])\d{,1}", Vencimento) :
                break
            else:
                print(">>> Vencimento inválido!, deve ser valor Real T8.2. <<<\n")
                continue

        f = open(_url_, "a+")
        print(
            IDF,
            CDF,
            NAME,
            IDC,
            IDT,
            IDS,
            IDFC,
            Email,
            Telemovel,
            NIF,
            NCC,
            DataAdmissao,
            Vencimento,
            sep=";",
            file=f
        )
        f.close()
        print("*** Funcionário foi inserido com sucesso! ***")

    # Others Importants Functions
    def Pesquisar():
        return True

    def Alterar():
        return True

    def Eliminar():
        return True

    def PesquisarOrdenar():
        return True

    def Contar():
        return True

    def Agrupar():
        return True

    def AgruparContar():
        return True

    def Exportar():
        return True

    def Organograma():
        return True
