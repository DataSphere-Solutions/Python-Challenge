# Importação da função sleep() para dar um efeito de "processando" no programa
from time import sleep

from datetime import datetime

# Declaração de variáveis de cores no terminal
limpaCor, cor_vermelho, cor_verde, cor_amarelo, cor_azul, cor_azul_claro = ('\033[m', '\033[31m', '\033[32m',
                                                                            '\033[33m', '\033[34m','\033[36m')

def linha(tam: int) -> str:
    """
    Retorna uma linha horizontal com o tamanho do parâmetro passado.
    """
    return '--' * tam


def cabecalho(txt: str) -> None:
    """
    Mostra na tela um texto formatado entre duas linhas horizontais, formando um cabeçalho.
    """
    print(linha(42))
    print(txt.center(42 * 2))
    print(linha(42))


# Lista com as opções de menu principal e menu dos itens que serão passadas como parâmetro para a função menu()
opcoes_menu = ['Alunos', 'Apresentações', 'Visitas', 'Passeios escolares', 'Sair do sistema']
opcoes_item = ['Visualizar dados', 'Adicionar novo item', 'Remover um item',
               'Limpar todos os dados do arquivo', 'Retornar para o menu principal']

def menu(opcoes: list, menu_principal = False) -> None:
    """
    Mostra o menu de opções formatado na tela.
    """
    if menu_principal:
        cabecalho('Data Sphere - Sistema de Registro para as Escolas')
        sleep(0.5)
    for i in range(len(opcoes)):
        print(f'{cor_amarelo}{i + 1} {limpaCor}- {cor_azul}{opcoes[i]}{limpaCor}')


def opcao(opc: int) -> int:
    """
    Mostra na tela o menu de subopções de cada item, e retorna a escolha do usuário do submenu
    """
    cabecalho(opcoes_menu[opc])
    menu(opcoes_item)
    sleep(0.5)
    escolha = ler_int('Escolha a operação que deseja realizar com o item: ')
    if str(escolha) in '12345':
        return int(escolha)
    else:
        print(opcao_invalida())


def ler_int(txt) -> int:
    """
    Lê um número inteiro e trata o valor. A função só retorna o valor se for realmente um número inteiro.
    """
    while True:
        try:
            n = int(input(txt))
        except ValueError:
            print(f'{cor_vermelho}Número inválido.{limpaCor}')
        else:
            return n


def ler_dia(txt: str) -> int:
    """
    Lê um dia e trata o valor. A função só retorna o valor do dia se o valor for válido.
    """
    while True:
        dia = ler_int(txt)
        if 1 <= dia <= 31:
            return dia
        else:
            print(f'{cor_vermelho}Dia inválido. Tente novamente.{limpaCor}')


def ler_mes(txt: str) -> int:
    """
    Lê um mês e trata o valor. A função só retorna o valor do mês se o valor for válido.
    """
    while True:
        mes = ler_int(txt)
        if 1 <= mes <= 12:
            return mes
        else:
            print(f'{cor_vermelho}Mês inválido. Tente novamente.{limpaCor}')


def ler_ano(txt: str) -> int:
    """
    Lê um ano e trata o valor. A função só retorna o valor do ano se o valor for válido.
    """
    while True:
        ano = ler_int(txt)
        if len(str(ano)) != 4 or ano < 2024:
            print(f'{cor_vermelho}Ano inválido. Tente novamente.{limpaCor}')
        else:
            return ano


def ler_data(dia: int, mes: int, ano: int) -> bool:
    """
    Recebe os valores inteiros de dia, mês e ano, checa se a data é válida e retorna True ou False.
    """
    dia_str = str(dia)
    mes_str = str(mes)
    ano_str = str(ano)

    data_str = f'{dia_str}/{mes_str}/{ano_str}'

    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        if data < datetime.now():
            return False
        return True
    except ValueError:
        return False


def opcao_invalida() -> str:
    """
    Retorna uma string explicando que a opção digitada foi inválida.
    """
    return f'{cor_vermelho}Por favor, digite uma opção válida!{limpaCor}'


arquivo_alunos = 'alunos.txt'
arquivo_apresentacoes = 'apresentacoes.txt'
arquivo_visitas = 'visitas.txt'
arquivo_passeios = 'passeios.txt'
lista_arquivos = [arquivo_alunos, arquivo_apresentacoes, arquivo_visitas, arquivo_passeios]


def checar_arquivos(arquivos: list) -> None:
    """
    Recebe uma lista de arquivos e o passa como parâmetro para outra função.
    """
    for i in range(len(arquivos)):
        checar_arquivo(arquivos[i])
        sleep(1)


def checar_arquivo(arquivo: str) -> None:
    """
    Recebe o nome de um arquivo e checa se ele existe ou não. Caso não exista, é criado.
    """
    check = ler_arquivo(arquivo)
    if not check:
        print(f'{cor_vermelho}Arquivo {arquivo} não encontrado no sistema. Criando...{limpaCor}')
        sleep(1)
        criar_arquivo(arquivo)
    else:
        print(f'{cor_verde}Arquivo {arquivo} encontrado.{limpaCor}')


def criar_arquivo(arq: str) -> None:
    """
    Cria um arquivo com o nome do parâmetro passado.
    """
    try:
        with open(arq, 'w') as arquivo:
            arquivo.write('')
    except Exception:
        print(f'{cor_vermelho}Não foi possível criar o arquivo {arquivo}.{limpaCor}')
    else:
        print(f'{cor_verde}Arquivo {arq} criado com sucesso.{limpaCor}')


def ler_arquivo(arquivo:str) -> bool:
    """
    Recebe o nome de um arquivo como parâmetro e tenta ler seu conteúdo. Retorna True se conseguir, e False se não.
    """
    try:
        with open(arquivo, 'r') as arquivo:
            arquivo.read()
        return True
    except FileNotFoundError:
        print(f'{cor_vermelho}Não foi possível ler o arquivo {arquivo}.{limpaCor}')
        return False


def adicionar_item(arq: str, input_tema: str) -> None:
    """
    Recebe o nome de um arquivo e a opção selecionada pelo usuário, e adiciona os dados ao arquivo passado.
    """
    with open(arq, 'a', encoding='UTF-8') as arquivo:
        match input_tema:
            case 'Alunos':
                rm = ler_rm()
                nome = str(input('Digite o nome do aluno: ')).strip().upper()
                idade = ler_int('Digite a idade do aluno: ')
                arquivo.write(f'{rm},{nome},{idade}\n')
                print(f'{cor_verde}Dado salvo com sucesso.{limpaCor}')
            case 'Apresentações':
                while True:
                    tema = str(input('Tema da apresentação: ')).strip().upper()
                    if len(tema) > 50:
                        print(f'{cor_vermelho}Erro! Nome de tema muito grande.{limpaCor}')
                    else:
                        break
                while True:
                    dia = ler_dia('Dia da apresentação: ')
                    mes = ler_mes('Mês da apresentação: ')
                    ano = ler_ano('Ano da apresentação: ')
                    if ler_data(dia, mes, ano):
                        arquivo.write(f'{tema},{dia},{mes},{ano}\n')
                        print(f'{cor_verde}Dado salvo com sucesso.{limpaCor}')
                        break
                    else:
                        print(f'{cor_vermelho}Data inválida! Por favor tente novamente.{limpaCor}')
            case 'Visitas':
                nome_piloto = str(input('Nome do piloto: ')).strip().upper()
                while True:
                    dia = ler_dia('Dia da visita: ')
                    mes = ler_mes('Mês da visita: ')
                    ano = ler_ano('Ano da visita: ')
                    if ler_data(dia, mes, ano):
                        arquivo.write(f'{nome_piloto},{dia},{mes},{ano}\n')
                        print(f'{cor_verde}Dado salvo com sucesso.{limpaCor}')
                        break
                    else:
                        print(f'{cor_vermelho}Data inválida! Por favor tente novamente.{limpaCor}')
            case 'Passeios escolares':
                local = str(input('Local do passeio: ')).strip().upper()
                parceira = str(input('Marca parceira: ')).strip().upper()
                while True:
                    dia = ler_dia('Dia do pesseio: ')
                    mes = ler_mes('Mês do passeio: ')
                    ano = ler_ano('Ano do passeio: ')
                    if ler_data(dia, mes, ano):
                        arquivo.write(f'{local},{dia},{mes},{ano},{parceira}\n')
                        print(f'{cor_verde}Dado salvo com sucesso.{limpaCor}')
                        break
                    else:
                        print(f'{cor_vermelho}Data inválida! Por favor tente novamente.{limpaCor}')
    sleep(1)


def preencher_dados(arq: str) -> dict:
    """
    Recebe o nome de um arquivo como parâmetro, converte todos os dados do arquivo para um dicionário e o retorna.
    """
    with open(arq, 'r', encoding='UTF-8') as arquivo:
        dados = {}
        for linha_dados in arquivo:
            lista_linha = linha_dados.split(",")
            valores = []
            for i in range(1, len(lista_linha)):
                valores.append(lista_linha[i].replace("\n", ""))
            dados[lista_linha[0]] = valores
        return dados


def ler_itens(arq: str, input_tema: str) -> None:
    """
    Recebe o nome de um arquivo como parâmetro, a opção selecionada pelo usuário e mostra na tela os dados de
    maneira formatada.
    """
    cabecalho(f'Registros de {input_tema} no sistema')
    dados = preencher_dados(arq)
    if len(dados) == 0:
        print(f'{cor_vermelho}Nenhum dado encontrado no sistema!{limpaCor}')
        sleep(1)
    else:
        match input_tema:
            case 'Alunos':
                for chave, valor in dados.items():
                    print(f'{chave +':':<12} {valor[0]:>57}, {valor[1]} ANOS')
            case 'Apresentações':
                for chave, valor in dados.items():
                    print(f'TEMA: {chave:<49} {'DATA: ' + valor[0]:>15}/{valor[1]}/{valor[2]}')
            case 'Visitas':
                for chave, valor in dados.items():
                    print(f'PILOTO: {chave:<49} {'DATA: ' + valor[0]:>15}/{valor[1]}/{valor[2]}')
            case 'Passeios escolares':
                for chave, valor in dados.items():
                    print(f'LOCAL: {chave:<28} {'DATA: ' + valor[0] + '/' + valor[1] + '/' + valor[2]:>12}'
                          f' {'PARCEIRA: ' + valor[3]:>25}')
    sleep(2)


def remover_item(arq: str, input_tema: str) -> None:
    """
    Recebe o nome de um arquivo e a opção selecionada pelo usuário, e remove o dado selecionado.
    """
    with open(arq, 'r') as arquivo:
        if len(arquivo.read()) == 0:
            print(f'{cor_vermelho}Arquivo vazio. Impossível realizar alterações.{limpaCor}')
            sleep(1.5)
            return
    dados = preencher_dados(arq)
    print(linha(42))
    for i, (chave, valor) in enumerate(dados.items()):
        print(f'{i + 1} - {chave}: {valor}')
    input_usuario = ler_int('Digite o índice do item que deseja remover: ')
    print(linha(42))
    chaves = list(dados.keys())
    if 1 <= input_usuario <= len(chaves):
        chave_remover = chaves[input_usuario - 1]
        dados.pop(chave_remover)
        print(f'{cor_verde}Item removido com sucesso: {chave_remover}{limpaCor}')
        sleep(1.5)
        with open(arq, 'w', encoding='UTF-8') as arquivo:
            match input_tema:
                case 'Alunos':
                    for chave, valor in dados.items():
                        arquivo.write(f'{chave},{valor[0]},{valor[1]}\n')
                case 'Apresentações':
                    for chave, valor in dados.items():
                        arquivo.write(f'{chave},{valor[0]},{valor[1]},{valor[2]}\n')
                case 'Visitas':
                    for chave, valor in dados.items():
                        arquivo.write(f'{chave},{valor[0]},{valor[1]},{valor[2]}\n')
                case 'Passeios escolares':
                    for chave, valor in dados.items():
                        arquivo.write(f'{chave},{valor[0]},{valor[1]},{valor[2]},{valor[3]}\n')
    else:
        print(f'{cor_vermelho}Índice inválido. Tente novamente.{limpaCor}')


def limpar_arquivo(arq: str):
    """
    Recebe o nome de um arquivo como parâmetro e limpa todo o seu conteúdo.
    """
    confirmar = str(input(f'{cor_vermelho}Deseja mesmo apagar todos os dados deste arquivo?'
                          f' Digite "SIM" para confirmar. {limpaCor}')).strip().upper()
    if confirmar == 'SIM':
        with open(arq, 'w') as arquivo:
            arquivo.write('')
        print(f'{cor_verde}Todos os dados do arquivo {arq} foram apagados com sucesso.{limpaCor}')
    else:
        print(f'{cor_vermelho}Operação cancelada.{limpaCor}')
        return


def ler_rm() -> str:
    """
    Trata o dado do RM e o retorna devidamente tratado.
    """
    while True:
        rm = str(input('Digite o RM do Aluno: ')).strip().upper().replace("RM", "")
        with open(arquivo_alunos, 'r', encoding='UTF-8') as alunos:
            if len(rm) != 6:
                print(f'{cor_vermelho}O RM do aluno deve possuir exatamente 6 números.{limpaCor}')
            elif rm in alunos.read():
                print(f'{cor_vermelho}RM já registrado no sistema. Por favor insira outro RM.{limpaCor}')
            else:
                break
    if "RM" not in rm:
        rm = "RM" + rm
    return rm
