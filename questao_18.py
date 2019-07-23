# TP1 - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 17/02/2019 - Thonny IDE
# questao_18

import psutil

memory_total = (psutil.virtual_memory().total)
memory_swap = (psutil.swap_memory().total)

print ("Memória total: " + (str(round(memory_total / (1024 * 1024 * 1024), 2)) + "GB"))
print ("Memória swap: " + (str(round(memory_swap / (1024 * 1024 * 1024), 2)) + "GB"))