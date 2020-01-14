import re

import json
import array
from array import array
import os.path
from os import path
import webbrowser
import os
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

    def Pesquisar(urlLang):
        _url_ = 'Dados/Funcionarios.csv'
        _L = json.loads(inFile.read(urlLang))
        attr = _L['attr']
        c = 1
        print('\n')
        for name in attr :
            print(str(c) + " - " + name)
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
            arr = []
            while k == 0 or len(s) > 0:
                s = inFile.line(k,_url_)
                if len(s) > 0:
                    qA = (s.split(";")[n-1]).lower()
                    qB = q.lower()
                    if qA.find(qB) > -1 :
                        arr.append(k)
                k = k + 1

            if len(arr) > 0:
                for x in arr:
                    a = inFile.line(x,_url_)
                    a = a.split(";")
                    s = 20
                    print(
                        "%s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s" % 
                        (a[0][:s],a[1][:s],a[2][:s],a[3][:s],a[4][:s],a[5][:s],a[6][:s], 
                        a[7][:s],a[8][:s],a[9][:s],a[10][:s],a[11][:s],a[12][:s])
                    )
            else:
                print('\n>>> ' + attr[n-1] + ' '+_L['no_found']+'! <<<')
            
        return True

    def Alterar(urlLang):
        _url_ = 'Dados/Funcionarios.csv'
        _L = json.loads(inFile.read(urlLang))
        attr = _L['attr']

        print('\n')
        f = open(_url_, "r", encoding='utf-8')
        k = 0
        while True :
            row = f.readline()
            if len(row) > 0:
                if k % 3 == 0:
                    a = attr
                    s = 8
                    print(
                        "[%s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s]\n" % 
                        (a[0][:s],a[1][:s],a[2][:s],a[3][:s],a[4][:s],a[5][:s],a[6][:s], 
                        a[7][:s],a[8][:s],a[9][:s],a[10][:s],a[11][:s],a[12][:s])
                    )
                a = row.split(';')
                s = 13
                print(
                    "%s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s" % 
                    (a[0][:s],a[1][:s],a[2][:s],a[3][:s],a[4][:s],a[5][:s],a[6][:s], 
                    a[7][:s],a[8][:s],a[9][:s],a[10][:s],a[11][:s],a[12][:s])
                )
                k = k + 1
            else:
                break

        while True:
            m = input('\nID Funcionario a alterar? ')
            RSLT = isValid.IDF(m, _url_)
            if RSLT == '-2':
                break
            else:
                if RSLT == 'True':
                    print('>>> O ID do Funcionário não existe! <<<')
                if RSLT == '-1':
                    print('>>> Caracteres Inválidos! <<<')
        print('\n')
        arr = []
        k = 1
        for x in attr:
            tmp = input(str(k)+' - '+x+'? ')
            if len(tmp) > 0:
                arr.append(tmp)
                k = k + 1
            else:
                arr.append('')

        inFile.update(m,arr,_url_)
        print('Alterado com sucesso!')

        return True

    def Eliminar(urlLang):
        _url_ = 'Dados/Funcionarios.csv'
        _L = json.loads(inFile.read(urlLang))
        attr = _L['attr']

        print('\n')
        f = open(_url_, "r", encoding='utf-8')
        k = 1
        while True :
            r = -1
            s = 15
            row = f.readline()
            if len(row) > 0:
                a = row.split(';')
                w = (a[0][:s],a[1][:s],a[2][:s],a[3][:s],a[4][:s],a[5][:s],a[6][:s],a[7][:s],a[8][:s],a[9][:s],a[10][:s],a[11][:s],a[12][:s])
                l = len(input( str(k) + " - %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s Selecionar ? " % w ))
                if l > 0:
                    while True:
                        r = input("\n\n>>> %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s\bDeseja apagar ( 1 - Sim | 0 - Não )? " % w)
                        if r=='1' or r=='0':
                            if r == '1':
                                inFile.export(a) # exportar os dados apagados!
                                inFile.delete(a[0],_url_)
                                print('>>> Apagado com sucesso! <<<')
                            print('\n')
                            break
                k = k + 1
            else:
                break

        return True

    def PesquisarOrdenar(urlLang):
        _url_ = 'Dados/Funcionarios.csv'
        _L = json.loads(inFile.read(urlLang))
        attr = _L['attr']
        c = 1
        print('\n')
        for name in attr :
            print(str(c) + " - " + name)
            c = c + 1
        n = input("\nOrdenar Por? ")
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
            p = 0
            arr = []
            while True:
                data = inFile.line(p,_url_)
                d = data.split(';')
                p = p + 1
                try:
                    val = d[n-1]
                    tid = str(p)
                    arr.append({val:tid})
                except:
                    print('')

                if len(data) < 1 :
                    break

            arr.sort()

            for x in arr:
                n = int(x.split(';')[1])
                rows = inFile.line(n,_url_)
                s = 20
                if len(rows) > 0:
                    a = rows.split(';')
                    w = (a[0][:s],a[1][:s],a[2][:s],a[3][:s],a[4][:s],a[5][:s],a[6][:s],a[7][:s],a[8][:s],a[9][:s],a[10][:s],a[11][:s],a[12][:s])
                    print("%s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s" % w )
            
        return True

    def Contar(urlLang):
        _url_ = 'Dados/Funcionarios.csv'
        _L = json.loads(inFile.read(urlLang))
        attr = _L['attr']

        print('\n')
        f = open(_url_, "r", encoding='utf-8')
        k = 1
        arrA = []
        arrB = []
        arrC = []
        while True :
            row = f.readline()
            if len(row) > 0:
                arrA.append(row.split(';')[0])
                arrB.append(row.split(';')[6])
                arrC.append(row.split(';')[2])
            else:
                break

        c = 0
        i = 0
        cat = ''
        for x in arrA:
            n = 0
            for y in arrB:
                if x == y:
                    n = n + 1
            if n > 0:
                c = c + 1
                cat = cat + ">>> "+arrC[i] + " Tem " + str(n) + " funcionários.\n"
            i = i + 1
        print( "\nFuncionários coordenadores ( %d )" % c )
        print(cat)

        return True

    def Agrupar(urlLang):
        _L = json.loads(inFile.read(urlLang))
        attr = _L['attr']
        x = 0
        print('\n')

        ff = open('Dados/Funcionarios.csv', "r", encoding='utf-8')
        fc = open('Dados/Categorias.csv', "r", encoding='utf-8')

        d1 = fc.readlines()
        d2 = ff.readlines()
        arr = []
        for k in range(len(d1)):
            c1 = 0
            dd1 = d1[k].split(' ')
            for l in range(len(d2)):
                dd2 = d2[l].split(';')
                if dd1[0] == dd2[3]:
                    arr.append(dd1[2])
                    break

            if len(arr)>0:
                print( 'A categoria ['+str(arr[len(arr)-1]).replace('\n','')+'] tem Funcionário!' )
        
        ff.close()
        fc.close()
        return True

    def AgruparContar(urlLang):
        _L = json.loads(inFile.read(urlLang))
        attr = _L['attr']
        x = 0
        print('\n')

        ff = open('Dados/Funcionarios.csv', "r", encoding='utf-8')
        fc = open('Dados/Categorias.csv', "r", encoding='utf-8')

        d1 = fc.readlines()
        d2 = ff.readlines()

        for k in range(len(d1)):
            c1 = 0
            dd1 = d1[k].split(' ')
            for l in range(len(d2)):
                dd2 = d2[l].split(';')
                if dd1[0] == dd2[3]:
                    c1 = c1 + 1
                    
            print( '> A categoria ['+str(dd1[2]).replace('\n','')+'] tem '+str(c1)+' Funcionário!' )
        
        ff.close()
        fc.close()
        return True

    def Exportar(urlLang):
        print('\n')
        # MacOS
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        # Linux
        chrome_path = '/usr/bin/google-chrome %s'
        # Windows
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        osCommandString = "notepad.exe "
        while True:
            print('1 - Visualizar TXT')
            print('2 - Visualizar CSV')
            print('3 - Visualizar HTML')
            r = input('\nEscolha uma das opções? ')
            if r == '1':
                tipo = 'txt'
                os.system(osCommandString+'Dados/exportados/ficheiro.txt')
                break
            elif r == '2':
                os.system('start excel.exe Dados/exportados/ficheiro.csv')
                break
            elif r == '3':
                webbrowser.get(chrome_path).open('Dados/exportados/ficheiro.html')
                break

        return True

    def Organograma(urlLang):
        _L = json.loads(inFile.read(urlLang))
        return True
