
count = 0
while count < 10:
    print(count)
    count += 1

# Nekonečný cyklus dosiahneme pomocou while True
count = 0
while True:
    print(count)


# Ukončiť cyklus vieme pomocou slova break
count = 0
while True: 
    print(count) 
    if count >= 10:
        break
    count += 1

# break pre ukončenie vo for cykle
for i in [1,2,3,4]:
    print(i)
    if i == 2:
        break

# continue na ukončenie aktuálnej iterácie, nie celého cyklu
count = 0
while True:  
    if count == 6:
        count += 1
        continue
    if count >= 25:
        break
    print(count)
    count += 1

# continue vo for cykle
for value in [1,2,3,4,5,6,7,8,9,10]:
    if value == 8:
        continue
    print(value)



