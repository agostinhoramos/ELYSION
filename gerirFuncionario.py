import re

import json
import os.path
from os import path

from Fn import isValid
from Fn import inFile
from Fn import _f

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
        
        CDF = _f.intToChar( inFile.NextLine(_url_) ) #Gerado Automaticamente!

        while True:
            NAME = input("Nome Completo do Funcionário? ")
            if re.search("^[A-Z][a-zA-Z]{3,}(?: [A-Z][a-zA-Z]*){0,4}$", NAME ) :
                break
            else:
                print(">>> Nome inválido!, [2-5] Palavras <<<\n")
                continue
        
        while True:
            IDC = input("ID Categoria? ")
            RSLT = isValid.IDC(IDC)
            if RSLT == 'True':
                break
            else:
                if RSLT == '-1':
                    print('\n>>> Código inválido!, [inteiro ate 4 digitos] <<<')
                elif RSLT == '-2':
                    print('\n>>> A categoria introduzida não existe! <<<')
                continue

        while True:
            IDT = input("ID Título? ")
            RSLT = isValid.IDT(IDT)
            if RSLT == 'True':
                break
            else:
                if RSLT == '-1':
                    print('\n>>> Código inválido!, [inteiro ate 4 digitos] <<<')
                elif RSLT == '-2':
                    print('\n>>> O título introduzido não existe! <<<')
                continue

        while True:
            IDS = input("ID Serviço? ")
            RSLT = isValid.IDS(IDS)
            if RSLT == 'True':
                break
            else:
                if RSLT == '-1':
                    print('\n>>> Código inválido!, [inteiro ate 4 digitos] <<<')
                elif RSLT == '-2':
                    print('\n>>> O serviço introduzido não existe! <<<')
                continue

        while True:
            if path.exists(_url_):
                IDFC = input("ID Funcionário chefe? ")
            else:
                print("ID Funcionário chefe? "+IDF)
                IDFC = IDF
                break
            RSLT = isValid.IDFC(IDFC)
            if RSLT == 'True':
                break
            else:
                if RSLT == '-1':
                    print('\n>>> Código inválido!, [inteiro ate 8 digitos] <<<')
                elif RSLT == '-2':
                    print('\n>>> O "ID Funcionário chefe" introduzido não existe! <<<')
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

    def Pesquisar(_url_ = 'Dados/Funcionarios.csv'):
        attr = json.loads(inFile.read('lang/pt-pt.json'))['attr']
        c = 1
        print('\n')
        for name in attr :
            print("\t"+ str(c) + " - " + name)
            c = c + 1
        n = input("\nSelecione a opção de Pesquisa? ")
        if not isValid.INT(n):
            n = 0
        while True:
            n = int(n)
            if n >= 0 and n <= c:
                break
            else:
                print('>>> Opção incorreta! <<<')
                if n == 0:
                    continue
                else:
                    break

        if n > 0 and n <= c:
            q = input("\n" + attr[n-1] + ' a pesquisar? ')
            k = 0
            pos = -1
            while k == 0 or len(s) > 0:
                s = inFile.line(k,_url_)
                if len(s) > 0:
                    if s.split(";")[int(n)-1] == q:
                        pos = k
                        break
                k = k + 1

            if pos >= 0:
                a = inFile.line(pos,_url_).split(";")
                print(
                        "\n[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]" % 
                        (a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12])
                    )
            else:
                print('\n>>> ' + attr[n-1] + ' não encontramos! <<<')
            
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
