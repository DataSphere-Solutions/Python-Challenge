# Importando as funções e variáveis criadas no arquivo funcies.py para o arquivo .py principal
from funcoes import *

# Função para caso os arquivos necessários para registrar os dados não existam, cria automaticamente
validarArquivos(arqAlunos, arqApresentacoes, arqVisitas, arqPasseios)

# Função com o conteúdo do programa principal
menu()
