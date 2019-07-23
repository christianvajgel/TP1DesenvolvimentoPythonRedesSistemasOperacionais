# TP1 - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 17/02/2019 - Thonny IDE
# questao_13

import subprocess

process = subprocess.Popen("cmd")
print("PID Processo Externo:", process.pid)