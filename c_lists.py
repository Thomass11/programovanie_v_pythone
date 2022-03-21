
# Zoznam - list
my_list = ["Jonathan Toews", "Brent Seabrook", "29", 50, 46.29, [25, 39, "Scores"]]

# Vrátenie dĺžky zoznamu
len(my_list)

# Vymazanie položky zoznamu 
del my_list[0]

# remove vymaže prvý výskyt znaku 
my_list.remove("29") 
print(my_list)

# count vráti počet výskytu daného prvku
print(my_list.count("Brent Seabrook"))

# index vráti pozíciu prvého výskytu daného prvku 
print(my_list.index("Brent Seabrook"))

# Pridanie položky zoznamu na koniec
my_list.append("Marian Hossa")
print(my_list)

# Insert vloží druhý prvok v zátvorke na pozíciu 4
my_list.insert(4, "Erik Gustafsson") 
print(my_list)

# Funkcia extend rozbalí zoznam a pridá na koniec listu
my_list.extend(["Joe Quenneville", 200, 300]) 
print(my_list)

# Funkcia reverse obráti poradie v zozname
my_list.reverse()
print(my_list)

# Upravovať vieme aj pomocou zloženého indexu
my_list=[0,1,2,3,4,5]

my_list[1:3] 
# Nahradíme prvky s indexom 1 a 2
my_list[1:3] = [20, 25]
print(my_list)
# Pridáme položky s indexom 3 a 4
my_list[1:3] = [30, 40, 50, 60]
print(my_list)
# Odstránime prvok s indexom 1 a 2
my_list[1:3] = []
print(my_list[1:3])


# Vráti poslednú položku zoznamu
print(my_list[-1])
# my_list[-2] vráti predposlednú (-2) položku zoznamu
print(my_list[-2])

# Funkcia pop vráti posledný prvok z listu a zmaže ho
my_list=[1,2,3,4,5]
my_list.pop()
print(my_list)

# Na nasčítanie nových prvkov musíme výsledok operácie priradiť
# do premennej, ináč sa pôvodná premenná nezmení 
my_list = [0,1,2,3,4,5]
my_list += [30, 40]
print(my_list)
# priradenie do premennej
my_list_new = my_list + [50, 70]
print(my_list_new)


my_list = [1, 7, 10, 29, 14, -6, 58]
new_list = []

# Vráti zoznam párnych čísel
for number in my_list:
    if number % 2 == 0:
        new_list.append(number)

print(new_list)

# Rovnaký zápis - list comprehension
new_list = [number for number in my_list if number % 2 == 0]
print(new_list)

# Vráti zoznam mien hráčov, ktorých dĺžka je viac ako 12 znakov
my_list = ["Jonathan Toews", "Brent Seabrook", "Patrick Kane", "Joe"]
new_list = [name for name in my_list if len(name) > 12]
print(new_list)


my_list = ["Tomas", "Toews", "50", "Kane", "False", "tatar@email.com", "bondra@email.com", "21", "46","Hossa Marian", "halak@email.com"] 

new_list = [value for value in my_list if value.isnumeric() ]
print(new_list)


# Nájdi v zozname len čísla a e-mailovú adresu a vypíš ich do nového zoznamu

my_list = ["Tomas", "Toews", 50, ["Patrik", "Rybar"], "Kane", "False", "tatar@email.com", "bondra@email.com", 21, "46.5","Hossa Marian", 
"halak@email.com"] 

new_list = [value for value in new_list if str(value).isnumeric() or str(value).find("@") > 0]
print(new_list)
