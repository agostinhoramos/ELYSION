import re

import json
import os.path
from os import path

from Fn import isValid
from Fn import inFile
from Fn import _f

class GF:
    def Inserir(urlLang):
        _url_ = 'Dados/Funcionarios.csv'
        _L = json.loads(inFile.read(urlLang))

        while True:
            IDF = input(_L['attr'][0]+"? ")
            RSLT = isValid.IDF(IDF, _url_)
            if RSLT == 'True' :
                break
            else:
                if RSLT == '-1':
                    tmp = _L['invalid_code']+'! [1-8] '+_L['digit']+', '+_L['the_init_val_more_0']+'.'
                    print('>>> '+tmp+' <<<\n')
                elif RSLT == '-2':
                    tmp = _L['already-exist-SOME-with-THIS'] % (_L['menu'][0], _L['this'][0]+" "+_L['code']+'!' )
                    print( '>>> '+tmp+' <<<\n' )
                continue
        
        CDF = _f.intToChar( inFile.NextLine(_url_) ) #Gerado Automaticamente!

        while True:
            NAME = input(_L['attr'][2]+"? ")
            if re.search("^[A-Z][a-zA-Z]{3,}(?: [A-Z][a-zA-Z]*){0,4}$", NAME ) :
                break
            else:
                tmp = _L['invalid_name']+'!, [2-5] '+_L['words']+'.'
                print(">>> "+tmp+" <<<\n")
                continue
        
        while True:
            IDC = input(_L['attr'][3]+"? ")
            RSLT = isValid.IDC(IDC)
            if RSLT == 'True':
                break
            else:
                if RSLT == '-1':
                    tmp = _L['inv-int-to-INT-digits'] % ('4')
                    print('\n>>> '+tmp+'! <<<')
                elif RSLT == '-2':
                    tmp = _L['the-NAME-insrt-no-exist'] % (_L['attr'][3])
                    print('\n>>> '+tmp+'! <<<')
                continue

        while True:
            IDT = input(_L['attr'][4]+"? ")
            RSLT = isValid.IDT(IDT)
            if RSLT == 'True':
                break
            else:
                if RSLT == '-1':
                    tmp = _L['inv-int-to-INT-digits'] % ('4')
                    print('\n>>> '+tmp+'! <<<')
                elif RSLT == '-2':
                    tmp = _L['the-NAME-insrt-no-exist'] % (_L['attr'][4])
                    print('\n>>> '+tmp+'! <<<')
                continue

        while True:
            IDS = input(_L['attr'][5]+"? ")
            RSLT = isValid.IDS(IDS)
            if RSLT == 'True':
                break
            else:
                if RSLT == '-1':
                    tmp = _L['inv-int-to-INT-digits'] % ('4')
                    print('\n>>> '+tmp+'! <<<')
                elif RSLT == '-2':
                    tmp = _L['the-NAME-insrt-no-exist'] % (_L['attr'][5])
                    print('\n>>> '+tmp+'! <<<')
                continue

        while True:
            if path.exists(_url_):
                IDFC = input(_L['attr'][6]+"? ")
            else:
                print(_L['attr'][6]+"? "+IDF)
                IDFC = IDF
                break
            RSLT = isValid.IDFC(IDFC)
            if RSLT == 'True':
                break
            else:
                if RSLT == '-1':
                    tmp = _L['inv-int-to-INT-digits'] % ('8')
                    print('\n>>> '+tmp+'! <<<')
                elif RSLT == '-2':
                    tmp = _L['the-NAME-insrt-no-exist'] % (_L['attr'][6])
                    print('\n>>> '+tmp+'! <<<')
                continue

        while True :
            Email = input(_L['attr'][7]+"? ")
            if re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", Email) :
                break
            else:
                print(">>> "+(_L['this'][0])+" "+_L['attr'][7]+" "+_L['invalid']+"! <<<\n")
                continue

        while True:
            Telemovel = input(_L['attr'][8]+"? ")
            if re.search( "(9[1236]\d{7})+$", Telemovel) :
                break
            else:
                print(">>> "+(_L['attr'][8])+" "+_L['invalid']+", "+_L['prefix']+" 91, 92, 93, 96! <<<\n")
                continue

        while True:
            NIF = input((_L['attr'][9])+"? ")
            RSLT = isValid.NIF(NIF)
            if RSLT == 'True' :
                break
            else:
                if RSLT == '-1':
                    print('>>> '+_L['int_only']+', 8 '+_L['digit']+'! <<<\n')
                elif RSLT == '-2':
                    print('>>> '+_L['attr'][9]+' '+_L['invalid']+'! <<<\n')

                continue
            
        while True:
            NCC = input(_L['attr'][10]+" [00000000 0 AA0]? ")
            RSLT = isValid.NCC(NCC)
            if RSLT == 'True':
                break
            else:
                if RSLT == '-1':
                    print(">>> "+_L['format']+" "+_L['invalid']+"!, [eg. 18170480 3 ZZ8] <<<\n")
                elif RSLT == '-2':
                    print('>>> '+_L['attr'][10]+' '+_L['invalid']+'! <<<\n')
                continue

        while True :
            DataAdmissao = input(_L['attr'][11]+" [YYYY MM DD hh mm ss]? ")
            RSLT = isValid.DATE(DataAdmissao)
            if RSLT == 'True':
                break
            else:
                if RSLT == '-1':
                    print('>>> '+_L['format']+' '+_L['invalid']+'! [YYYY MM DD hh mm ss] <<<\n')
                elif RSLT == '-2':
                    print('>>> '+_L['insert_less_iqual_current']+'! <<<\n')
                continue

        while True:
            Vencimento = input((_L['attr'][12])+"? ")
            if re.search("([0-9])\d{,7}\.([0-9])\d{,1}", Vencimento) :
                break
            else:
                print(">>> "+(_L['attr'][12])+" "+_L['invalid']+"!, T8.2. <<<\n")
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
        print("*** "+(_L['menu'][0])+" "+_L['was-insert-sucess']+"! ***")

    def Pesquisar(_url_ = 'Dados/Funcionarios.csv'):
        attr = _L['attr']
        c = 1
        print('\n')
        for name in attr :
            print("\t"+ str(c) + " - " + name)
            c = c + 1
            tmp = _L['select-the-opction-of']+' '+(_L['opc'][2])
        n = input("\n"+tmp+"? ")
        if not isValid.INT(n):
            n = 0
        while True:
            n = int(n)
            if n >= 0 and n <= c:
                break
            else:
                print('>>> '+_L['option'] + ' ' +_L['invalid']+'! <<<')
                if n == 0:
                    continue
                else:
                    break

        if n > 0 and n <= c:
            q = input("\n" + attr[n-1]+' '+(_L['to'][1])+' '+(_L['opc'][2])+'? ')
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
                print('\n>>> ' + attr[n-1] + ' '+_L['no_found']+'! <<<')
            
        return True

    def Alterar(urlLang):
        return True

    def Eliminar(urlLang):
        return True

    def PesquisarOrdenar(urlLang):
        return True

    def Contar(urlLang):
        return True

    def Agrupar(urlLang):
        return True

    def AgruparContar(urlLang):
        return True

    def Exportar(urlLang):
        return True

    def Organograma(urlLang):
        return True
