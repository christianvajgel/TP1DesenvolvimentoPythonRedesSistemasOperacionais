# TP1 - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 17/02/2019 - Thonny IDE
# questao_15

import psutil
import time

pid = int(input("Entre com o número do PID: "))
process = psutil.Process(pid)
print("")

print("O usuário ", process.username(), "foi quem iniciou o processo.")
print("O processo foi criado em ", time.ctime(process.create_time()))
print("O processo consumiu ", round(process.memory_info().rss / 1024, 2), "KB de memória.")