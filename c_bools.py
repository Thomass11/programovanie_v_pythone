

# Dátový typ bool ma len dve hodnoty True a False
my_true_value = True
my_false_value = False

# Výstupom porovnávacích oeprácií je dátový typ (True/False)
5 < 9
510 > 650
21 == 21
21 < 30
8 == 8.0
911 != 12

# Na zistenie rovnosti vždy používa dvojité '=' 
x = 11
11 == 11.0

# porovnávať vieme aj premenné
num1 = 21
num2 = 500
num1 >= num2

# Bool vieme aj negovať pomocou funkcie not
my_var =True
not(my_var)

# Porovnávacie operácie vieme reťazit logickými operátormi and, or 
21 < 22 and 21 > 20
21 < 22 or 21 > 20
not(21 < 22 and 22 > 24)


# Cvičenie - skús uhádnuť pravdivostnú hodnotu následne to over v Pythone
not(4 <= 16) and 5 > 7 
17 != 14 or 4 > 6
9 == 8 and 3 <= 2
10 >= 13 and 4 != 3 or 12 < 14
not(3 > 6) or not(4 == 18 or 7 > 8) 


num1 = 1
num2 = 20
result = ""

result = "A" if num1 > num2 else "B" if num1 < num2 else "C"

print(result)
