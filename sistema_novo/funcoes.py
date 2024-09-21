# Importação da função sleep() para dar um efeito de "processando" no programa
from time import sleep

# Declaração de variáveis de cores no terminal
limpaCor, cor_vermelho, cor_verde, cor_amarelo, cor_azul, cor_azul_claro = ('\033[m', '\033[31m', '\033[32m', '\033[33m', '\033[34m',
                                                        '\033[36m')

# Função que retorna uma linha de acordo com o tamanho desejado
def linha(tam):
    return '--' * tam


# Função que printa um cabeçalho com o texto centralizado, entre duas linhas horizontais
def cabecalho(txt):
    print(linha(42))
    print(txt.center(42 * 2))
    print(linha(42))


# Lista com as opções que serão passadas como parâmetro para a função menu()

opcoes_menu = ['Alunos', 'Apresentações', 'Visitas', 'Passeios escolares', 'Sair do sistema']
opcoes_item = ['Visualizar dados', 'Adicionar novo item', 'Remover um item',
               'Limpar todos os dados do arquivo', 'Retornar para o menu principal']

def menu(opcoes):
    if opcoes_menu[1] == 'Alunos':
        cabecalho('Data Sphere - Sistema de Registro para as Escolas')
        sleep(0.5)
    for i in range(len(opcoes)):
        print(f'{cor_amarelo}{i + 1} {limpaCor}- {cor_azul}{opcoes[i]}{limpaCor}')


def opcao(opc):
    cabecalho(opcoes_menu[opc])
    menu(opcoes_item)
    sleep(0.5)
    escolha = ler_int('Escolha a operação que deseja realizar com o item: ')
    if str(escolha) in '12345':
        return int(escolha)
    else:
        print(opcao_invalida())


# Função que lê um input de um número inteiro sem dar erro e crashar o programa
def ler_int(txt):
    while True:
        try:
            n = int(input(txt))
        except ValueError:
            print(f'{cor_vermelho}Número inválido.{limpaCor}')
        else:
            return n


def opcao_invalida():
    return f'{cor_vermelho}Por favor, digite uma opção válida!{limpaCor}'


arquivo_alunos = 'alunos.txt'
arquivo_apresentacoes = 'apresentacoes.txt'
arquivo_visitas = 'visitas.txt'
arquivo_passeios = 'passeios.txt'
lista_arquivos = [arquivo_alunos, arquivo_apresentacoes, arquivo_visitas, arquivo_passeios]


def checar_arquivos(arquivos):
    for i in range(len(arquivos)):
        checar_arquivo(arquivos[i])
        sleep(1)


def checar_arquivo(arquivo):
    check = ler_arquivo(arquivo)
    if not check:
        print(f'{cor_vermelho}Arquivo {arquivo} não encontrado no sistema. Criando...{limpaCor}')
        sleep(1)
        criar_arquivo(arquivo)
    else:
        print(f'{cor_verde}Arquivo {arquivo} encontrado.{limpaCor}')


def criar_arquivo(arq):
    try:
        with open(arq, 'w') as arquivo:
            arquivo.write('')
    except Exception:
        print(f'{cor_vermelho}Não foi possível criar o arquivo {arquivo}.{limpaCor}')
    else:
        print(f'{cor_verde}Arquivo {arq} criado com sucesso.{limpaCor}')


def ler_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as arquivo:
            arquivo.read()
        return True
    except FileNotFoundError:
        print(f'{cor_vermelho}Não foi possível ler o arquivo {arquivo}.{limpaCor}')
        return False


def adicionar_item(arq, input_tema):
    with open(arq, 'a', encoding='UTF-8') as arquivo:
        match input_tema:
            case 'Alunos':
                rm = ler_rm()
                nome = str(input('Digite o nome do aluno: ')).strip().upper()
                idade = ler_int('Digite a idade do aluno: ')
                arquivo.write(f'{rm},{nome},{idade}\n')
            case 'Apresentações':
                while True:
                    tema = str(input('Tema da apresentação: ')).strip().upper()
                    if len(tema) > 50:
                        print(f'{cor_vermelho}Erro! Nome de tema muito grande.{limpaCor}')
                    else:
                        break
                dia = ler_int('Dia da apresentação: ')
                mes = ler_int('Mês da apresentação: ')
                ano = ler_int('Ano da apresentação: ')
                arquivo.write(f'{tema},{dia},{mes},{ano}\n')
            case 'Visitas':
                nome_piloto = str(input('Nome do piloto: ')).strip().upper()
                dia = ler_int('Dia da visita: ')
                mes = ler_int('Mês da visita: ')
                ano = ler_int('Ano da visita: ')
                arquivo.write(f'{nome_piloto},{dia},{mes},{ano}\n')
            case 'Passeios escolares':
                local = str(input('Local do passeio: ')).strip().upper()
                dia = ler_int('Dia do passeio: ')
                mes = ler_int('Mês do passeio: ')
                ano = ler_int('Ano do passeio: ')
                parceira = str(input('Marca parceira: ')).strip().upper()
                arquivo.write(f'{local},{dia},{mes},{ano},{parceira}\n')
    sleep(1)


def preencher_dados(arq):
    with open(arq, 'r', encoding='UTF-8') as arquivo:
        dados = {}
        for linha in arquivo:
            lista_linha = linha.split(",")
            valores = []
            for i in range(1, len(lista_linha)):
                valores.append(lista_linha[i].replace("\n", ""))
            dados[lista_linha[0]] = valores
        return dados


def ler_itens(arq, input_tema, alterar=False):
    cabecalho(f'Registros de {input_tema} no sistema')
    dados = preencher_dados(arq)
    if len(dados) == 0:
        print(f'{cor_vermelho}Nenhum dado encontrado no sistema!{limpaCor}')
        sleep(1)
    else:
        i = 1
        match input_tema:
            case 'Alunos':
                for chave, valor in dados.items():
                    if alterar:
                        print(f'{i}. ', end='')
                    print(f'{chave +':':<12} {valor[0]:>57}, {valor[1]} ANOS')
                    i += 1
            case 'Apresentações':
                for chave, valor in dados.items():
                    if alterar:
                        print(f'{i}. ', end='')
                    print(f'TEMA: {chave:<49} {'DATA: ' + valor[0]:>15}/{valor[1]}/{valor[2]}')
                    i += 1
            case 'Visitas':
                for chave, valor in dados.items():
                    if alterar:
                        print(f'{i}. ', end='')
                    print(f'PILOTO: {chave:<49} {'DATA: ' + valor[0]:>15}/{valor[1]}/{valor[2]}')
                    i += 1
            case 'Passeios escolares':
                for chave, valor in dados.items():
                    if alterar:
                        print(f'{i}. ', end='')
                    print(f'LOCAL: {chave:<28} {'DATA: ' + valor[0] + '/' + valor[1] + '/' + valor[2]:>12}'
                          f' {'PARCEIRA: ' + valor[3]:>25}')
                    i += 1
    sleep(2)


def remover_item(arq, input_tema):
    with open(arq, 'r') as arquivo:
        if len(arquivo.read()) == 0:
            print(f'{cor_vermelho}Arquivo vazio. Impossível realizar alterações.{limpaCor}')
            sleep(1.5)
            return
    dados = preencher_dados(arq)
    for i, (chave, valor) in enumerate(dados.items()):
        print(f'{i + 1} - {chave}: {valor}')
    input_usuario = ler_int('Digite o índice do item que deseja remover: ')
    chaves = list(dados.keys())
    if 1 <= input_usuario <= len(chaves):
        chave_remover = chaves[input_usuario - 1]
        dados.pop(chave_remover)
        print(f'Item removido com sucesso: {chave_remover}')
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
    print(dados)


def limpar_arquivo(arq):
    confirmar = str(input(f'{cor_vermelho}Deseja mesmo apagar todos os dados deste arquivo?'
                          f' Digite "SIM" para confirmar. {limpaCor}')).strip().upper()
    if confirmar == 'SIM':
        with open(arq, 'w') as arquivo:
            arquivo.write('')
        print(f'{cor_verde}Todos os dados do arquivo {arq} foram apagados com sucesso.{limpaCor}')
    else:
        print(f'{cor_vermelho}Operação cancelada.{limpaCor}')
        return


def ler_rm():
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
