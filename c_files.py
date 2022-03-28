# Súbor sa otvorí pomocou funkcie open
# Vždy je ho nutné zavrieť, my_file.close()
# Alebo použiť kontext manažér

file_read = open("FileFolder/test_file.txt", "r")
print(file_read)
file_read.close() # Zavrieť súbor !


# Funkcia readline číta znak za znakom v súbore
file_read = open("FileFolder/test_file.txt", "r")
print(file_read.readline(1))
print(file_read.readline(1))
file_read.close() 


# Kontext manažér
with open("FileFolder/test_file.txt", "r") as my_file:
    for read_f in my_file:
        print(read_f, end="")


with open("tomas_tatar.txt", "w") as my_file:
    for my_string in ["Tomas", "Tatar", "hra", "za", "New Jersey", "Devils"]:
        my_file.write(my_string)
        my_file.write("\n")

data_file = []
with open("FileFolder/tomas_tatar.txt", "r") as my_file:
    for read_f in my_file:
        data_file.append(read_f)

print(data_file)

with open("FileFolder/reversed_tomas_tatar.txt", "w") as my_file:
    for read_l in reversed(data_file):
        my_file.write(read_l)
       # my_file.write("\n")

# Úloha - napíš aplikáciu, ktorá obráti riadky a slová v danom riadku
# Vstup:
# Tomas
# Tatar - cislo 21
# hra

# Výstup:
# arh
# 12 olsic - rataT
# samoT

with open("FileFolder/total_reversed_tomas_tatar.txt", "w") as my_file:
    for read_l in reversed(data_file):
        for read_w in reversed(read_l):
            my_file.write(read_w)

data_file = ["od", "roku", "2019"]
with open("FileFolder/tomas_tatar.txt", "a") as my_file:
    for read_l in data_file:
        # Precastovanie kvôli tomu, všetko v súbore je string
        my_file.write(str(read_l)) 
        my_file.write("\n")


my_file = open("FileFolder/test_file.txt", "r")

# Vypísanie obsahu súboru
while True:
    actual_char = my_file.readline()

    # Ak dosiahneme koniec súboru
    if not actual_char:
        break

    print(actual_char, end="")

line_counter = 0

for line in my_file:
    line_counter += 1

my_file.close()
print(str(line_counter))


# Spočíta počet slov v súbore
my_file = open("FileFolder/test_file.txt", "r")

word_counter = 0

for line in my_file:
    # Split funkcia vráti list z každého riadku v súbore
    # Slová rozdelí na základe medzery 
    words = line.split()
    # len funkcia dĺžku listu
    word_counter += len(words)

my_file.close()

print(str(word_counter))


# Iterácia cez viac súborov
counter = 0
for val in [1, 2, 3, 4]:
    with open(f"FileFolder/{val}.txt", "r") as my_file:
        for line in my_file:
            words = line.split()
            counter += len(words)

print(str(counter))


# Počet výskytu slova v súbore
my_file = open("FileFolder/test_file.txt", "r")

counter = 0

for line in my_file:
    words = line.split()
    # result = [word for word in words if word.lower() == "riadok"]
    counter += len([word for word in words if word.lower() == "číslo"])  
    # print(result)

my_file.close()

print(str(counter))