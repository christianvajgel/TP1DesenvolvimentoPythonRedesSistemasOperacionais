# TP1 - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 17/02/2019 - Thonny IDE
# questao_19

import psutil
import os

print ("Partição do sistema: ", psutil.disk_partitions()[0][0])
print ("Valor livre para armazenamento: ", round(psutil.disk_usage('C:\\').free / (1024 * 1024 * 1024), 2), " GB")