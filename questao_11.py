# TP1 - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 17/02/2019 - Thonny IDE
# questao_11

import subprocess

file = input("Entre com o nome do arquivo: ") + ".txt"

subprocess.run(["notepad", file])