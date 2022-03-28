
points = [10, -5, 0, 4, 35, -25, 42.5, 100]
# sorted funkcia vrátilist v stúpajúcom poaradí
sorted(points)

# sorted funkcia vráti list v klesajúcom poaradí
print(sorted(points, reverse=True))

# sorted funkcia vráti v abecednom poradí
# použitím reverse parametra, vráti list v opačnom poradí
players_names = ["Patrick", "Jonathan", "Brendon", "Joe"]
print(sorted(players_names))


# Triedenie podľa dĺžky reťazca
# od najmenšieho po najväčšie
teams = ["Washington Cap", "Chiccago Blackhakws", "Boston B", "LA"]
teams = sorted(teams, key=len)
print(teams)

# Triedenie v zozname
# index hovorí, či triediť podľa key alebo value
def dict_sorter(x):
    return x[0]

players = {"Patrick_Kane": 88, "Jonathan_Toews": 16, 
"Brendon_Saad": 20, "Erik_Gustafsson": 56}

# Vrátené tuple v zozname
result = sorted(players.items(), key=dict_sorter)
print(result)

