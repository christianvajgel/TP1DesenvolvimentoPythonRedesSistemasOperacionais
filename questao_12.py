# TP1 - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 17/02/2019 - Thonny IDE
# questao_12

import os
import subprocess

subprocess.call(['notepad.exe', 'text_file.txt'])
subprocess.Popen(['notepad.exe'])

path = os.environ['SYSTEMROOT'] + '\\System32\\cmd.exe'
os.spawnl(os.P_WAIT, path, " ")