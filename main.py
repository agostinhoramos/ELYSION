# by ELYSION - Algoritmo e Estrutura de Dados 2020
'''
Agostinho de Pina Ramos - 1012444
Erickson Rompão - 1702282
'''
import json
from Fn import inFile

from gerirFuncionario import GF
from gerirServico import GS
from gerirCategoria import GC
from gerirTitulo import GT

def menu():
    while True:
        opc = input("\n[ 1 - English | 2 - Portuguese ]? ")
        if opc == '1':
            urlLang = 'lang/en-us.json'
            break
        elif opc == '2':
            urlLang = 'lang/pt-pt.json'
            break
    _L = json.loads(inFile.read(urlLang))
    opc = '0'
    while opc == '0':
        print('\n\t+++++ '+_L['main_menu']+' +++++\n')
        a = _L['menu']
        k = 1
        for d in a:
            print(str(k) + ' - ' + d)
            k = k + 1

        x = input(_L['choose_option']+': ')
        if x == '1':          # main menu <<<-------
            opc = '1'
            while opc == '1' :
                print('\n\t+++++ ' + (_L['menu'][0]) + ' +++++')
                a = _L['opc']
                k = 0
                for d in a:
                    print(str(k) + ' - ' + d)
                    k = k + 1
                x = input(_L['choose_option']+': ')
                if x == '1':
                    GF.Inserir(urlLang)
                elif x == '2':
                    GF.Pesquisar(urlLang)
                elif x == '3':
                    GF.Alterar(urlLang)
                elif x == '4':
                    GF.Eliminar(urlLang)
                elif x == '5':
                    GF.PesquisarOrdenar(urlLang)
                elif x == '6':
                    GF.Contar(urlLang)
                elif x == '7':
                    GF.Agrupar(urlLang)
                elif x == '8':
                    GF.AgruparContar(urlLang)
                elif x == '9':
                    GF.Exportar(urlLang)
                elif x == '10':
                    GF.Organograma(urlLang)
                elif x == '0':
                    opc = x
                else:
                    print("\n>>> "+_L['invalid_option']+"! <<<")
                
                if opc == '1':
                    while True:
                        tmp = _L['want_continue'] % (_L['with']+' '+_L['menu'][0])
                        opc = input("\n"+tmp+" (1 - "+_L['yes']+" "+_L['or']+" 0 - "+_L['no']+")? ")
                        if not (opc == '1' or opc == '0'):
                            print('>>> (1 - '+_L['yes']+' '+_L['or']+' 0 - '+_L['no']+')? <<<\n')
                            continue
                        else:
                            print("\n")
                            break
                else:
                    print("\n")
        elif x == '2':          # main menu <<<-------
            opc = '1'
            while opc == '1' :
                print('\n\t+++++ ' + (_L['menu'][1]) + ' +++++')
                a = _L['opc']
                k = 0
                for d in a:
                    print(str(k) + ' - ' + d)
                    k = k + 1
                x = input(_L['choose_option']+': ')
                if x == '1':
                    GS.Inserir(urlLang)
                elif x == '2':
                    GS.Pesquisar(urlLang)
                elif x == '3':
                    GS.Alterar(urlLang)
                elif x == '4':
                    GS.Eliminar(urlLang)
                elif x == '5':
                    GS.PesquisarOrdenar(urlLang)
                elif x == '6':
                    GS.Contar(urlLang)
                elif x == '7':
                    GS.Agrupar(urlLang)
                elif x == '8':
                    GS.AgruparContar(urlLang)
                elif x == '9':
                    GS.Exportar(urlLang)
                elif x == '10':
                    GS.Organograma(urlLang)
                elif x == '0':
                    opc = x
                else:
                    print("\n>>> "+_L['invalid_option']+"! <<<")
                
                if opc == '1':
                    while True:
                        tmp = _L['want_continue'] % (_L['with']+' '+_L['menu'][1])
                        opc = input("\n"+tmp+" (1 - "+_L['yes']+" "+_L['or']+" 0 - "+_L['no']+")? ")
                        if not (opc == '1' or opc == '0'):
                            print('>>> (1 - '+_L['yes']+' '+_L['or']+' 0 - '+_L['no']+')? <<<\n')
                            continue
                        else:
                            print("\n")
                            break
                else:
                    print("\n")
        elif x == '3':          # main menu <<<-------
            opc = '1'
            while opc == '1' :
                print('\n\t+++++ ' + (_L['menu'][2]) + ' +++++')
                a =  _L['opc']
                k = 0
                for d in a:
                    print(str(k) + ' - ' + d)
                    k = k + 1
                x = input(_L['choose_option']+': ')
                if x == '1':
                    GS.Inserir(urlLang)
                elif x == '2':
                    GS.Pesquisar(urlLang)
                elif x == '3':
                    GS.Alterar(urlLang)
                elif x == '4':
                    GS.Eliminar(urlLang)
                elif x == '5':
                    GS.PesquisarOrdenar(urlLang)
                elif x == '6':
                    GS.Contar(urlLang)
                elif x == '7':
                    GS.Agrupar(urlLang)
                elif x == '8':
                    GS.AgruparContar(urlLang)
                elif x == '9':
                    GS.Exportar(urlLang)
                elif x == '10':
                    GS.Organograma(urlLang)
                elif x == '0':
                    opc = x
                else:
                    print("\n>>> "+_L['invalid_option']+"! <<<")
                
                if opc == '1':
                    while True:
                        tmp = _L['want_continue'] % (_L['with']+' '+_L['menu'][2])
                        opc = input("\n"+tmp+" (1 - "+_L['yes']+" "+_L['or']+" 0 - "+_L['no']+")? ")
                        if not (opc == '1' or opc == '0'):
                            print('>>> (1 - '+_L['yes']+' '+_L['or']+' 0 - '+_L['no']+')? <<<\n')
                            continue
                        else:
                            print("\n")
                            break
                else:
                    print("\n")
        elif x == '4':          # main menu <<<-------
            opc = '1'
            while opc == '1' :
                print('\n\t+++++ ' + (_L['menu'][3]) + ' +++++')
                a =  _L['opc']
                k = 0
                for d in a:
                    print(str(k) + ' - ' + d)
                    k = k + 1
                x = input(_L['choose_option']+': ')
                if x == '1':
                    GS.Inserir(urlLang)
                elif x == '2':
                    GS.Pesquisar(urlLang)
                elif x == '3':
                    GS.Alterar(urlLang)
                elif x == '4':
                    GS.Eliminar(urlLang)
                elif x == '5':
                    GS.PesquisarOrdenar(urlLang)
                elif x == '6':
                    GS.Contar(urlLang)
                elif x == '7':
                    GS.Agrupar(urlLang)
                elif x == '8':
                    GS.AgruparContar(urlLang)
                elif x == '9':
                    GS.Exportar(urlLang)
                elif x == '10':
                    GS.Organograma(urlLang)
                elif x == '0':
                    opc = x
                else:
                    print("\n>>> "+_L['invalid_option']+"! <<<")
                
                if opc == '1':
                    while True:
                        tmp = _L['want_continue'] % (_L['with']+' '+_L['menu'][3])
                        opc = input("\n"+tmp+" (1 - "+_L['yes']+" "+_L['or']+" 0 - "+_L['no']+")? ")
                        if not (opc == '1' or opc == '0'):
                            print('>>> (1 - '+_L['yes']+' '+_L['or']+' 0 - '+_L['no']+')? <<<\n')
                            continue
                        else:
                            print("\n")
                            break
                else:
                    print("\n")

        if opc == '0':
            while True:
                tmp = _L['want_exit'] % (_L['from']+' '+_L['mn'])
                opc = input("\n"+tmp+"(1 - "+_L['yes']+" "+_L['or']+" 0 - "+_L['no']+")? ")
                if not (opc == '1' or opc == '0'):
                    print('>>> (1 - '+_L['yes']+' '+_L['or']+' 0 - '+_L['no']+')? <<<\n')
                    continue
                else:
                    print("\n")
                    break
        else:
            print("\n")

# call main function!
menu()