

# Funkcia range vytvára akési počítadlo <dolný interval; horný interval)
count = range(0, 10)
print(count)

# Vieme definovať, o koľko sa prvok v počítadle zvýši/zníži
range(0, 10, 2)
range(10, 1, -2)

# Skončí s výpisom 9
for num in range(0, 10, 1):
    print(num)

for num in range(20, 0, -2):
    print(num)

# Pole
nums = [1, 2, 3, 4, 5, 10]

# Vieme prechádzať cez polia
for num in nums:
    print(num)

# Vieme prechádzať cez reťazce
for value in "Chicago Blackhawks":
    print(value) 


# Vieme iterovať cez akékoľvek pole 
values = ["Patrick", 16.23, "Jonathan", [1, 9], "Brent", "Joe", 25, "Marian"]
for value in values:
    print(value)


# Do cyklu vieme pridať aj podmienky alebo vnorený cyklus
values = ["Patrick", "Joe", "Brendon", "Jonathan"]
for value in values:
    if value == 'Joe':
        for num in range (0, 5, 1):
            print(num)


values = ["Patrick", "Joe", "Brandon"]
for key, value in enumerate(values):
    print(str(key) + " " + str(value))


# Alebo takýto zápis
values = ["Patrick", "Joe", "Brandon"]
for  value in values:
    print(str(value))
