
# Funkcia na sčítavanie
def join_parametres(a, b):
    result = a + b
    return result

join_parametres(21, 14)
join_parametres("Tomas" , "Tatar")

# Funkciu môžeme aj reťaziť
join_parametres(join_parametres(21, 14), 56)
join_parametres(join_parametres(join_parametres(join_parametres("Tomas" , "Tatar"), "is"), "NHL"), "player")


# Funkcia, ktorá vráti súčet zoznamu (list)
nums = list(range(21))
print(nums)

def sum_numbers(nums):
    total = 0 
    for num in nums:
        total += num
    return total

sum_numbers(nums)
sum(nums) # Python funkcia


# Funkcie vieme použiť aj v podmienke
if sum_numbers(nums) > 100:
    print("List is bigger than 100")
else:
    print("List is not bigger than 100")

# Funkcie vieme použiť v zozname (list) 
[join_parametres("Tomas" , "Tatar"), join_parametres("Tomas" , "Jurco"), 21, join_parametres("Jonathan" , "Toews")]


# definícia funkcie s povinnými argumentami name a age, nepovinným player_number
def show_name(name, age, player_number = 99, club = "NHL"):
    #lokálna premenná
    club = "Chicago Blackhawks"
    print(f"Player name is: {name} with age: {age} and player number: {player_number} in the club: {club}")

show_name("Jonathan Toews", 32)


# definícia funkcie s neznánym počtom argumentov
def show_player_details(*details):
    goals = 2 * details[3]
    print(f"Player name is {details[0]} with age: {details[1]} in the club: {details[2]}")
    print(f"Goals: {goals}")

show_player_details("Brent Seabrook", 31, "Chicago Blackhawks", 29)


def show_players(*players):
    for index in range(len(players)):
        print(players[index])

show_players("Jonathan Toews", "Brent Seabrook", "Corey Crawford", "Erik Gustafsson")


# definícia funkcie s náhodným počtom kľúčvých argumentov key->value
def show_profile(**profile):
    print(f"Player name: {profile['name']} with age: {profile['age']} in th club: {profile['club']}")

show_profile(name = "Erik Gustafsson", age = 28, club = "Chicago Blackhawks")

def show_club(name, age, player_number, club = "Chicago Blackhawsk"):
    print(f"Player name: {name} with age: {age} and the player number: {player_number} in the club: {club} ")

show_club("Erik Gustafsson", 28, 56)


# definícia funkcie s návratovou hodnotou, vráti súčet zoznamu
points = list(range(10))
print(points)

def sum_points(points):
    total = 0 
    for point in points:
        total += point
    return total


sum_points(points)
sum(points) # Python funkcia 


# definícia funkcie s viacerými návratovými hodnotami
# vráti Tuple
def score(point):
    if point % 2 == 0:
        return 1, True
    else:
        return 0, False

p1, p2 = score(20), score(21)
print(p1)
print(p2)



# definícia funkcie s vrátenou sekvenciou hodnôt 
# kľúčové slovo return vráti chybu
def score():
    for point in range(0, 10, 1):
        if point % 2 == 0:
            yield point

for point in score():
    print(point)


# definícia funkcie s prázdnym telom 
def show_club():
    pass

c = 10

def handle_variable():
    a = 20
    # z premmenj c vytvoríme globálnu premennnú použitím global
    global c
    c = 15

# prememná a je lokálna premenná
# Python vráti chybu
print(a)

# prememná c je globálna premenná
# Python vráti 15
handle_variable()
print(c)



