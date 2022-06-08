# Daemanom a bezne vlakna

import threading as thr 

# =======1 uloha========
# Na zaciatku Python virtual machine (PVM), vytvara Main vlakno a z neho vytvara dcerske vlakno
# print(thr.current_thread().getName())

# # V tomto priklade, Hlavne vklakno vytvara 2 dcerske vlakna,
# # ktore sa nazyvaju ako aplikacne vlakna
# t1 = thr.Thread()
# t2 = thr.Thread()

# =======2 uloha========

def normal_operation():
    for i in range(10000):
        print("Bežné vlákno je spustené")

def daemon_operation():
    while True:
        print("Dameon vlákno je spustené")

t1 = thr.Thread(target=normal_operation, name="Worker thread")

# Deamon vlakno ukonci operaciu, ked bezne vlakna ukoncia operaciu
# Po 1000 iteraciah bezneho vlakna, Python prerusi / ukonci Daemnon vlakno
# aj napriek tomu, ak je v nekonecnej slucke, a skonci sa program
t2 = thr.Thread(target=daemon_operation, name="Daemon thread", daemon=True)

t1.start()
t2.start()



