# Importando as funções e variáveis criadas no arquivo funcies.py para o arquivo .py principal
from funcoes import *

# Função para caso os arquivos necessários para registrar os dados não existam, cria automaticamente
validar_arquivos(arq_alunos, arq_apresentacoes, arq_visitas, arq_passeios)

# Função com o conteúdo do programa principal
programa_principal()
