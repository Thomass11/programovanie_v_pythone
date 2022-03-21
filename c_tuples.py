
# Toto je Tuple
my_tuple = ("Jonathan Toews", "Patrick Kane", "Joe Quenneville", 40, 22.6, -1)

# Toto nefunguje, Tuple je immutable dátový typ
my_tuple[2] = "Erik Gustafsson"

# Výpis Tuple
print(my_tuple[2])

# Ina definícia Tuple
my_tuple = 1,2,3,4,5

# Tuple ako návratová hodnota z funkcie
def return_my_tupple(var1, var2):
    return var1, var1
return_my_tupple("Chicago", "Blackhawks")

# Spojenie (join) Tuple
tuple1 = ("Erik", "Joe" , "Brandon")
tuple2 = ("Gustafsson", "Queneville", "Saad")

tuple3 = tuple1 + tuple2
print(tuple3)

