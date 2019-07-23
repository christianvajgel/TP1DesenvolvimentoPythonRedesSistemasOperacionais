# TP1 - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 17/02/2019 - Thonny IDE
# questao_20

import psutil

print ("Partição corrente: ", psutil.disk_partitions())
print ("Sistema de arquivo: ", psutil.disk_partitions()[3][2])
print ("Valor total para armazenamento: ", round(psutil.disk_usage('/').total / (1024 * 1024 * 1024), 2), " GB")
print ("Valor livre para armazenamento: ", round(psutil.disk_usage('/').free / (1024 * 1024 * 1024), 2), " GB")