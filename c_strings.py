
# String môžeme definovat pomocou dvojitých, jednoduchých úvodzoviek
my_variable = "This is my string 1"
my_variable2 =' This is my string 2'

# String vieme vypísať pomocou funkcie print
print(my_variable)
print(21)
# print(21.5)
print(True)
number = 81
print(number)

# String vieme definovať aj na viac riadkov
my_variable ="""
This is  
multiline 
string.
Cross lines.
"""
print(my_variable)

# \n je symbol na vloženie nového riadku
my_variable="This is string with \nnew line"
print(my_variable)

# Použitím r pred definíciou stringu, nevloží nový riadok
my_path=r"C:\documents\notes"
print(my_path)


my_string = "This is my string 1"
print(my_string)
print(my_string[0])
print(my_string[2:])
print(my_string[-1])
print(my_string[-4:])

# Funkcia len vráti dĺžku stringu
print(len(my_string))

# Zreťazenie (sčítanie) stringov
name = "Tomas"
space = " "
surname = "Tatar"
person_name = name + space + surname
print(person_name)

# Bez použitia medzery
print(name, surname)


# Metóda count () vracia počet výskytu hodnoty  v reťazci
txt = "Tomas Tatar is New Jersey Devils player in NHL, Jersey"

value = txt.count("Jersey", 25)

print(value)


# Metóda find () vyhľadá prvý výskyt hľadanej hodnoty
# Metóda index, vráti index hľdandého prvku
print(txt.find("NHL"))
print(txt.index("r"))

# Metóda lower () vráti reťazec, v ktorom sú všetky znaky malé
print(txt.lower())


# Metóda join () zoberie všetky položky do iterovateľnej formy a spojí ich do jedného reťazca.
my_variable = "This is my string 1"
my_variable2 =' This is my string 2'
print(my_variable.join(my_variable2))


# Metóda split () rozdelí reťazec na zoznam (list)
my_string = "10840;Gillian-Hardwicke;Gillian.Hardwicke@email.com;2400"
employee = my_string.split(";")
print(employee)

# Metóda strip () odstráni všetky medzery na začiatku a na konci reťazca
input_text = "       User         "
value = input_text.strip()
print(f"Dĺžka reťazca je {len(value)} znakov, výstup: {value}")

