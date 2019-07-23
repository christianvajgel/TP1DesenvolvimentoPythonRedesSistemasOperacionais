# TP1 - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 17/02/2019 - Thonny IDE
# questao_6

import os

file = "questao_6.py"

if os.path.exists(file):
    print(file, " encontrado!")
    if os.path.isfile(file):
        print(file, " é um arquivo!")
        file_extension = os.path.splitext(file)
        print("A extensão do arquivo é " + file_extension [1])
else:
    print(file, " não encontrado!")
    print(file, " não é um arquivo!")