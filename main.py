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
    LANG = json.loads(inFile.read('lang/pt-pt.json'))
    opc = '0'
    while opc == '0':
        print('\n\t+++++ '+LANG['main_menu']+' +++++\n')
        a = LANG['menu']
        k = 1
        for d in a:
            print(str(k) + ' - ' + d)
            k = k + 1

        x = input(LANG['choose_option']+': ')
        if x == '1':          # main menu <<<-------
            opc = '1'
            while opc == '1' :
                print('\n\t+++++ ' + (LANG['menu'][0]) + ' +++++')
                a = LANG['opc']
                k = 0
                for d in a:
                    print(str(k) + ' - ' + d)
                    k = k + 1
                x = input(LANG['choose_option']+': ')
                if x == '1':
                    GF.Inserir()
                elif x == '2':
                    GF.Pesquisar()
                elif x == '3':
                    GF.Alterar()
                elif x == '4':
                    GF.Eliminar()
                elif x == '5':
                    GF.PesquisarOrdenar()
                elif x == '6':
                    GF.Contar()
                elif x == '7':
                    GF.Agrupar()
                elif x == '8':
                    GF.AgruparContar()
                elif x == '9':
                    GF.Exportar()
                elif x == '10':
                    GF.Organograma()
                elif x == '0':
                    opc = x
                else:
                    print("\n>>> " + (LANG['invalid_option']) + "! <<<")
                
                if opc == '1':
                    while True:
                        opc = input("\n"+LANG['want_continue']+" (1 - "+LANG['yes']+" "+LANG['or']+" 0 - "+LANG['no']+")? ")
                        if not (opc == '1' or opc == '0'):
                            print('>>> (1 - '+LANG['yes']+' '+LANG['or']+' 0 - '+LANG['no']+')? <<<\n')
                            continue
                        else:
                            print("\n")
                            break
                else:
                    print("\n")
        elif x == '2':          # main menu <<<-------
            opc = '1'
            while opc == '1' :
                print('\n\t+++++ ' + (LANG['menu'][1]) + ' +++++')
                a = LANG['opc']
                k = 0
                for d in a:
                    print(str(k) + ' - ' + d)
                    k = k + 1
                x = input(LANG['choose_option']+': ')
                if x == '1':
                    GS.Inserir()
                elif x == '2':
                    GS.Pesquisar()
                elif x == '3':
                    GS.Alterar()
                elif x == '4':
                    GS.Eliminar()
                elif x == '5':
                    GS.PesquisarOrdenar()
                elif x == '6':
                    GS.Contar()
                elif x == '7':
                    GS.Agrupar()
                elif x == '8':
                    GS.AgruparContar()
                elif x == '9':
                    GS.Exportar()
                elif x == '10':
                    GS.Organograma()
                elif x == '0':
                    opc = x
                else:
                    print("\n>>> "+LANG['invalid_option']+"! <<<")
                
                if opc == '1':
                    while True:
                        opc = input("\n"+LANG['want_continue']+" (1 - "+LANG['yes']+" "+LANG['or']+" 0 - "+LANG['no']+")? ")
                        if not (opc == '1' or opc == '0'):
                            print('>>> (1 - '+LANG['yes']+' '+LANG['or']+' 0 - '+LANG['no']+')? <<<\n')
                            continue
                        else:
                            print("\n")
                            break
                else:
                    print("\n")
        elif x == '3':          # main menu <<<-------
            opc = '1'
            while opc == '1' :
                print('\n\t+++++ ' + (LANG['menu'][2]) + ' +++++')
                a =  LANG['opc']
                k = 0
                for d in a:
                    print(str(k) + ' - ' + d)
                    k = k + 1
                x = input(LANG['choose_option']+': ')
                if x == '1':
                    GS.Inserir()
                elif x == '2':
                    GS.Pesquisar()
                elif x == '3':
                    GS.Alterar()
                elif x == '4':
                    GS.Eliminar()
                elif x == '5':
                    GS.PesquisarOrdenar()
                elif x == '6':
                    GS.Contar()
                elif x == '7':
                    GS.Agrupar()
                elif x == '8':
                    GS.AgruparContar()
                elif x == '9':
                    GS.Exportar()
                elif x == '10':
                    GS.Organograma()
                elif x == '0':
                    opc = x
                else:
                    print("\n>>> "+LANG['invalid_option']+"! <<<")
                
                if opc == '1':
                    while True:
                        opc = input("\n"+LANG['want_continue']+" (1 - "+LANG['yes']+" "+LANG['or']+" 0 - "+LANG['yes']+")? ")
                        if not (opc == '1' or opc == '0'):
                            print('>>> (1 - '+LANG['yes']+' '+LANG['or']+' 0 - '+LANG['no']+')? <<<\n')
                            continue
                        else:
                            print("\n")
                            break
                else:
                    print("\n")
        elif x == '4':          # main menu <<<-------
            opc = '1'
            while opc == '1' :
                print('\n\t+++++ ' + (LANG['menu'][3]) + ' +++++')
                a =  LANG['opc']
                k = 0
                for d in a:
                    print(str(k) + ' - ' + d)
                    k = k + 1
                x = input(LANG['choose_option']+': ')
                if x == '1':
                    GS.Inserir()
                elif x == '2':
                    GS.Pesquisar()
                elif x == '3':
                    GS.Alterar()
                elif x == '4':
                    GS.Eliminar()
                elif x == '5':
                    GS.PesquisarOrdenar()
                elif x == '6':
                    GS.Contar()
                elif x == '7':
                    GS.Agrupar()
                elif x == '8':
                    GS.AgruparContar()
                elif x == '9':
                    GS.Exportar()
                elif x == '10':
                    GS.Organograma()
                elif x == '0':
                    opc = x
                else:
                    print("\n>>> "+LANG['invalid_option']+"! <<<")
                
                if opc == '1':
                    while True:
                        opc = input("\n"+LANG['want_continue']+" (1 - "+LANG['yes']+" "+LANG['or']+" 0 - "+LANG['no']+")? ")
                        if not (opc == '1' or opc == '0'):
                            print('>>> (1 - '+LANG['yes']+' '+LANG['or']+' 0 - '+LANG['no']+')? <<<\n')
                            continue
                        else:
                            print("\n")
                            break
                else:
                    print("\n")

        if opc == '0':
            while True:
                opc = input("\n"+LANG['want_exit']+"(1 - "+LANG['yes']+" "+LANG['or']+" 0 - "+LANG['no']+")? ")
                if not (opc == '1' or opc == '0'):
                    print('>>> (1 - '+LANG['yes']+' '+LANG['or']+' 0 - '+LANG['no']+')? <<<\n')
                    continue
                else:
                    print("\n")
                    break
        else:
            print("\n")

# call main function!
menu()