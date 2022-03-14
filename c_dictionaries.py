my_dict = {
    'name': 'Tomas',
    'surname': 'Tatar',
    'number': 21,
    'EU_player': True,
    'teams': {'AHL': 'Grand Rapids', 'NHL': ['Detroit', 'Las Vegas', 'Montreal', 'New Jersey', 'Unknown']},
    'career': {
        'start': 'Dubnica nad Vahom',
        'NHL_start': 'Detroit',
        'now': 'New Jersey'
    }
}

# Kopírovanie slovníkov
new_dict = my_dict.copy()
print(new_dict)

# Výpis položiek key->value zo slovníka
for key, value in my_dict.items():
    print('Key is: ' + key + " and value is: " + str(value))

# Výpis položiek
print(my_dict['name'] + ' ' + my_dict['surname'])
print(my_dict['career']['now'])
print(my_dict['teams']['NHL'][-1])


# Výpis listu vo vnorenom slovníku
for item in my_dict['teams']['NHL']:
    print(item)

# Iný zápis
for i in range(len(my_dict['teams']['NHL'])):
  print(my_dict['teams']['NHL'][i])


# Prístup na základe kľúču, ktorý nevráti chybu, ak neexistuje
# Vieme definovať hodnotu, ktorú vráti, ak kľúč neexistuje 
my_dict.get('born')  
my_dict.get('not_existing_key', 'Key born not found') 

# keys vráti ako list kľúčov
my_dict.keys() 

# values vráti ako list hodnôt
# odporúča sa použiť ako zoznam - list(my_dict.values())
my_dict.values()

# items vráti všetko key->value slovníka ako list tuples 
list(my_dict.items())

# Vráti hodnotu kľúča a kľúč vymaže zo slovníka
my_dict.pop("number") 

# vymaže posledné key->value zo slovníka a vráti ho ako tuple 
my_dict.popitem()

# Vymazanie položky zo slovníka
del my_dict['EU_player']

# Pridanie položky do slovníka
my_dict['position'] = 'left wing'

my_dict =  dict(name='thomas', age =25)
print(my_dict)
