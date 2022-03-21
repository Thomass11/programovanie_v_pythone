
my_set = {"Tomas", "Tatar", 21, True, "Montreal"}

# Nefunguje, vráti chybu
# print(my_set[0])

# Výpis set: {True, 'Tatar', 21, 'Tomas', 'Montreal'}
# Poradie popložiek nie je zachované !
print(my_set)

# Kontrola výskytu položky
if "Tatar" in my_set:
    print("Found one")

for item in my_set:
    print(item)

# Pridanie položky
my_set.add("left wing")

# Pridanie viacerých položiek
my_set.update([29, "Detroit", False])


# Dĺžka set
len(my_set)

# remove() vs discard()
# remove() vráti chybu, ak položka neexistuje
# discard() nevráti chybu, ak položka neexistuje
my_set.discard("born")

# pop funkcia vráti poslednú NÁHODNÚ položku a vymaže ju
print(my_set.pop())

# union spojí 2 sets do jedného, odstráni DUPLICITY
set1 = {1, 10, "Joe"}
set2 = {1, "Joe", "Patrick" , "Kane", 29}
result = set1.union(set2)
print(result)

# Rozdiel dvoch sets vráti 10
set1 = {1, 10, "Joe"}
set2 = {1, "Joe", "Patrick" , "Kane", 29}
result = set1.difference(set2)
print(result)

