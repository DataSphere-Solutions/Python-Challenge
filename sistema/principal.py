# Importando as funções e variáveis criadas no arquivo init.py para o arquivo .py principal
# from sistema import *

# Importação da função sleep() para dar um efeito de "processando" no programa
from time import sleep

# Declaração de variáveis de cores no terminal
limpaCor, vermelho, verde, amarelo, azul, azulClaro = ('\033[m', '\033[31m', '\033[32m', '\033[33m', '\033[34m',
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
opcoes = ['Ver Registro de Alunos', 'Cadastrar novo Aluno', 'Ver Apresentações Agendadas', 'Agendar nova Apresentação',
          'Ver Visitas Agendadas', 'Agendar nova Visita', 'Ver Passeios Escolares Agendados',
          'Agendar novo Passeio Escolar', 'Sair do Sistema']


# Função que printa o menu de opções do sistema
def menu(opcoes):
    cabecalho('Sistema de Registro para as Escolas')
    for i in range(len(opcoes)):
        print(f'{amarelo}{i + 1} {limpaCor}- {azul}{opcoes[i]}{limpaCor}')


# Função que lê um input de um número inteiro sem dar erro e crashar o programa
def lerInt(txt):
    try:
        n = int(input(txt))
    except ValueError:
        print(f'{vermelho}Por favor, digite uma opção válida.{limpaCor}')
    else:
        return n


# Declaração das variáveis com os nomes dos arquivos necessários para o registro dos dados, para facilitar na escrita do
# código
arqAlunos = 'alunos.txt'
arqApresentacoes = 'apresentacoes.txt'
arqVisitas = 'visitas.txt'
arqPasseios = 'passeios.txt'


def validarArquivos(arqal, arqap, arqvis, arqpas):
    if not existeArquivo(arqal):
        criarArquivo(arqal)
    if not existeArquivo(arqap):
        criarArquivo(arqap)
    if not existeArquivo(arqvis):
        criarArquivo(arqvis)
    if not existeArquivo(arqpas):
        criarArquivo(arqpas)


# Função que checa se um arquivo existe ou não, retornando True se existe ou False caso não
def existeArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'{vermelho}Arquivo de registro {nome} não encontrado, criando...{limpaCor}')
        sleep(1.5)
        return False
    else:
        return True


# Função que cria um arquivo
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print(f'{vermelho}Erro! Não foi possível criar o arquivo.{limpaCor}')
    else:
        print(f'{verde}Arquivo de registro {nome} criado com sucesso!{limpaCor}')
        sleep(1.5)
    finally:
        a.close()


# Declaração de uma variável para facilitar na formatação dos dados que aparecerão no console
espaco = ''


def lerEscolha():
    while True:
        menu(opcoes)
        opcao = lerInt(f'{verde}Sua escolha: {limpaCor}')
        match opcao:
            case 1:
                lerArquivo(arqAlunos)
            case 2:
                cabecalho('Cadastrar novo Aluno')
                nome = str(input('Nome do aluno: ')).strip().capitalize()
                idade = lerInt('Idade do aluno: ')
                turma = str(input('Turma do aluno: ')).strip().upper()
                cadastrarAluno(arqAlunos, nome, idade, turma)
            case 3:
                lerArquivo(arqApresentacoes)
            case 4:
                cabecalho('Agendar nova Apresentação')
                tema = str(input('Tema/Conteúdo da Apresentação: ')).strip().capitalize()
                dia = lerInt('Dia: ')
                mes = lerInt('Mês: ')
                cadastrarApresentacao(arqApresentacoes, tema, dia, mes)
            case 5:
                lerArquivo(arqVisitas)
            case 6:
                cabecalho('Agendar nova Visita')
                nome_piloto = str(input('Nome do Piloto: ')).strip().capitalize()
                dia = lerInt('Dia: ')
                mes = lerInt('Mês: ')
                cadastrarVisita(arqVisitas, nome_piloto, dia, mes)
            case 7:
                lerArquivo(arqPasseios)
            case 8:
                cabecalho('Agendar novo Passeio Escolar')
                local = str(input('Local do Passeio: '))
                dia = lerInt('Dia: ')
                mes = lerInt('Mês: ')
                cadastrarPasseio(arqPasseios, local, dia, mes)
            case 9:
                print(linha(42))
                print(f'{vermelho}Obrigado por utilizar o sistema!{limpaCor}')
                break


# Função que lê o conteúdo de um arquivo
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'{vermelho}Erro! Não foi possível ler o arquivo.{limpaCor}')
    else:
        if nome == arqAlunos:
            cabecalho('Alunos Registrados no Sistema')
        elif nome == arqApresentacoes:
            cabecalho('Apresentações Agendadas no Sistema')
        elif nome == arqVisitas:
            cabecalho('Visitas Agendadas no Sistema')
        elif nome == arqPasseios:
            cabecalho('Passeios Escolares Agendados no Sistema')
        for linhas in a:
            dado = linhas.split(';')
            dado[2] = dado[2].replace('\n', '')
            if nome == arqAlunos:
                print(f'Nome: {dado[0]:<15} {espaco:>10}Idade: {dado[1]:>5} {espaco:>10}Turma: {dado[2]:>15}')
            elif nome == arqApresentacoes:
                print(f'Tema: {dado[0]:<50} {espaco:>15}Data: {dado[1]}/{dado[2]}\t')
            elif nome == arqVisitas:
                print(f'Nome do Piloto: {dado[0]:<40} {espaco:>15}Data: {dado[1]}/{dado[2]}\t')
            elif nome == arqPasseios:
                print(f'Local: {dado[0]:<48} {espaco:>15}Data: {dado[1]}/{dado[2]}\t')
        sleep(2)
    finally:
        a.close()


# Função que cadastra um novo aluno no sistema
def cadastrarAluno(arquivo, nome='desconhecido', idade=0, turma='desconhecida'):
    try:
        a = open(arquivo, 'at')
    except:
        print(f'{vermelho}Não foi possível adicionar o novo registro.{limpaCor}')
    else:
        a.write(f'{nome};{idade};{turma}\n')
        a.close()


# Função que agenda uma nova apresentação no sistema
def cadastrarApresentacao(arquivo, tema='desconhecido', dia=0, mes=0):
    try:
        a = open(arquivo, 'at')
    except:
        print(f'{vermelho}Não foi possível agendar a nova apresentação.{limpaCor}')
    else:
        a.write(f'{tema};{dia};{mes}\n')
        a.close()


def cadastrarVisita(arquivo, nome='desconhecido', dia=0, mes=0):
    try:
        a = open(arquivo, 'at')
    except:
        print(f'{vermelho}Não foi possível agendar a visita.{limpaCor}')
    else:
        a.write(f'{nome};{dia};{mes}\n')
        a.close()


def cadastrarPasseio(arquivo, local='desconhecido', dia=0, mes=0):
    try:
        a = open(arquivo, 'at')
    except:
        print(f'{vermelho}Não foi possível agendar o passeio.{limpaCor}')
    else:
        a.write(f'{local};{dia};{mes}\n')
        a.close()


# Função para caso os arquivos necessários para registrar os dados não existam, cria automaticamente
validarArquivos(arqAlunos, arqApresentacoes, arqVisitas, arqPasseios)

# Função com o conteúdo do programa principal
lerEscolha()
