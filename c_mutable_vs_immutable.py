
# Immutable int
x = 5
print(id(x))

# 140196051032496 - miesto v pamäti

# Vytvorí nové miesto v pamäti, novú premennú
# nepriradí hodnotu pôvodnej premennej
x = x + 1
print(id(x))
# 140196051032528 - nové miesto v pamäti

# Mutable objekt list
my_list = [1, 2, 3, 4]
print(id(my_list))
# 140196080602240 - miesto v pamäti

# Nevytvorí nové miesto v pamäti, a nový list,
# aktualizuje pôvodný list
my_list[0] = 10
print(id(my_list))
# 140196080602240 - pôvodné miesto v pamäti

