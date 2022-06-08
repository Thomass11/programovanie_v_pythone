import threading as thr

# Vrati nazov aktualneho vlakna
# vsetky ostatne vlakna su vytvoreneje z hlavneho vlakna MainThread
print(thr.current_thread().getName())

a = 10
b = 20

# MainThread vykona operacie sekvencne, vytvori premennu a,
# priradi hodnotu, vytvori prememnu b, priradi hodnotu
print(a, b)


def count_operation():
    for i in range(1000):
        print(thr.current_thread().getName() + " " + str(i))

# MainThread vykona prvu count operaciu, pocka kym skonci,
# potom vykona druhu count operaciu (sekvencne vykonanie)
# count_operation()
# count_operation()

# Vytvorenie vlakna
# Vyvorenie Thread triedy
# target - povie vlaknu, ktoru operaciu vykonat
# name - nazov vlakna
t1 = thr.Thread(target=count_operation, name="Patrick")
t2 = thr.Thread(target=count_operation, name="Joe")

# vdaka time-slicing, OS vykona obe operacie sucasne
t1.start()
t2.start()

