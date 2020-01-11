# by ELYSION - Algoritmo e Estrutura de Dados 2020
'''
Agostinho de Pina Ramos - 1012444
Erickson Rompão - 1702282
'''
from gerirFuncionario import GF
from gerirServico import GS
from gerirCategoria import GC
from gerirTitulo import GT

def menu():
    opc = '0'
    while opc == '0':
        print('\n\t+++++ Menu Principal +++++\n')
        print('1 - Funcionário')
        print('2 - Serviço')
        print('3 - Categoria')
        print('4 - Título')

        x = input('Escolha uma das opções: ')
        if x == '1':          # main menu <<<-------
            opc = '1'
            while opc == '1' :
                print('\n\t+++++ Funcionário +++++')
                print("1 - Inserir")
                print("2 - Pesquisar")
                print("3 - Alterar")
                print("4 - Eliminar")
                print("5 - Pesqusar e Ordenar")
                print("6 - Contar")
                print("7 - Agrupar")
                print("8 - Agrupar e Contar")
                print("9 - Exportar")
                print("10 - Gerar Organogramas")
                print("0 - Sair")
                x = input('Escolha uma das opções: ')
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
                    print("\n>>> Esta opção é inválida! <<<")
                
                if opc == '1':
                    while True:
                        opc = input("\nDeseja continuar (1 - Sim ou 0 - Não)? ")
                        if not (opc == '1' or opc == '0'):
                            print('>>> (1 - Sim ou 0 - Não)? <<<\n')
                            continue
                        else:
                            print("\n")
                            break
                else:
                    print("\n")
        elif x == '2':          # main menu <<<-------
            opc = '1'
            while opc == '1' :
                print('\n\t+++++ Serviço +++++')
                print("1 - Inserir")
                print("2 - Pesquisar")
                print("3 - Alterar")
                print("4 - Eliminar")
                print("5 - Pesqusar e Ordenar")
                print("6 - Contar")
                print("7 - Agrupar")
                print("8 - Agrupar e Contar")
                print("9 - Exportar")
                print("10 - Gerar Organogramas")
                print("0 - Sair")
                x = input('Escolha uma das opções: ')
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
                    print("\n>>> Esta opção é inválida! <<<")
                
                if opc == '1':
                    while True:
                        opc = input("\nDeseja continuar (1 - Sim ou 0 - Não)? ")
                        if not (opc == '1' or opc == '0'):
                            print('>>> (1 - Sim ou 0 - Não)? <<<\n')
                            continue
                        else:
                            print("\n")
                            break
                else:
                    print("\n")
        elif x == '3':          # main menu <<<-------
            opc = '1'
            while opc == '1' :
                print('\n\t+++++ Categoria +++++')
                print("1 - Inserir")
                print("2 - Pesquisar")
                print("3 - Alterar")
                print("4 - Eliminar")
                print("5 - Pesqusar e Ordenar")
                print("6 - Contar")
                print("7 - Agrupar")
                print("8 - Agrupar e Contar")
                print("9 - Exportar")
                print("10 - Gerar Organogramas")
                print("0 - Sair")
                x = input('Escolha uma das opções: ')
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
                    print("\n>>> Esta opção é inválida! <<<")
                
                if opc == '1':
                    while True:
                        opc = input("\nDeseja continuar (1 - Sim ou 0 - Não)? ")
                        if not (opc == '1' or opc == '0'):
                            print('>>> (1 - Sim ou 0 - Não)? <<<\n')
                            continue
                        else:
                            print("\n")
                            break
                else:
                    print("\n")
        elif x == '4':          # main menu <<<-------
            opc = '1'
            while opc == '1' :
                print('\n\t+++++ Título +++++')
                print("1 - Inserir")
                print("2 - Pesquisar")
                print("3 - Alterar")
                print("4 - Eliminar")
                print("5 - Pesqusar e Ordenar")
                print("6 - Contar")
                print("7 - Agrupar")
                print("8 - Agrupar e Contar")
                print("9 - Exportar")
                print("10 - Gerar Organogramas")
                print("0 - Sair")
                x = input('Escolha uma das opções: ')
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
                    print("\n>>> Esta opção é inválida! <<<")
                
                if opc == '1':
                    while True:
                        opc = input("\nDeseja continuar (1 - Sim ou 0 - Não)? ")
                        if not (opc == '1' or opc == '0'):
                            print('>>> (1 - Sim ou 0 - Não)? <<<\n')
                            continue
                        else:
                            print("\n")
                            break
                else:
                    print("\n")

        if opc == '0':
            while True:
                opc = input("\nDeseja sair (1 - Sim ou 0 - Não)? ")
                if not (opc == '1' or opc == '0'):
                    print('>>> (1 - Sim ou 0 - Não)? <<<\n')
                    continue
                else:
                    print("\n")
                    break
        else:
            print("\n")

# call main function!
menu()