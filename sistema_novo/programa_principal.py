from funcoes import *

checar_arquivos(lista_arquivos)

while True:
    menu(opcoes_menu)
    while True:
        input_usuario = ler_int('Digite uma opção que deseja consultar: ')
        if str(input_usuario) in '12345':
            break
        else:
            print(opcao_invalida())
    if input_usuario == 5:
        print(f'{cor_vermelho}Obrigado por utilizar o nosso sistema!{limpaCor}')
        break
    else:
        input_usuario -= 1
        while True:
            input_operacao = opcao(input_usuario)
            match input_operacao:
                case 1:
                    ler_itens(lista_arquivos[input_usuario], opcoes_menu[input_usuario])
                case 2:
                    adicionar_item(lista_arquivos[input_usuario], opcoes_menu[input_usuario])
                case 3:
                    remover_item(lista_arquivos[input_usuario], opcoes_menu[input_usuario])
                case 4:
                    limpar_arquivo(lista_arquivos[input_usuario], opcoes_menu[input_usuario])
                case 5:
                    break
