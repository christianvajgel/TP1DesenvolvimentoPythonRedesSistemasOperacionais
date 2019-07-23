# TP1 - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 17/02/2019 - Thonny IDE
# questao_8

import os

for root, dirs, files in os.walk("."):  
    for filename in files:
        print(filename)
        print(round(os.stat(filename).st_size / 1024), 1, "Kb")