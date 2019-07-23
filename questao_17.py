# TP1 - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 17/02/2019 - Thonny IDE
# questao_17

import psutil

for i in range(20):
    print("CPU: " + str(psutil.cpu_percent(interval = 1.0, percpu = False)) + " %")