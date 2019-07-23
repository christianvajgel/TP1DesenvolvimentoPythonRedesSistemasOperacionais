# TP1 - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 17/02/2019 - Thonny IDE
# questao_9

import os
import time

path = "."
 
files = os.listdir(path)
for name in files:
    print(name, "Data de criação: ", time.ctime(os.path.getctime(path)))
    print(name, "Data de modificação: ", time.ctime(os.path.getctime(path)))
    print("")