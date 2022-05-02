# Enkapsulácia

class Stadium:
    capacity = 15000
    __name = "United Center " # skrytie premennej

    def __init__(self, a, b):
        self.__a = a # skrytie premennej
        self.__b = b
    
    def __print_capacity(self): # skrytie metódy
        print(Stadium.capacity)

    def set_a(self, value):
        self.__a = value
    
    def get_a(self):
        return self.__a

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name
    
    def print_address(self):
        print(f"Address: {self.__a} {self.__b}")

arena = Stadium("1901 West Madison Street", "Chicago")
# Výpis vráti chybu, 
# nevieme pristúpiť k _name, rovnako ani k __a, __b
# print(Stadium.__name) 

# Prístup 1 k skrytým premenným
print(arena.get_a())
arena.set_a("Different address")
print(arena.get_a())

# Prístup 2 k skrytým premenným a k skrytej metóde
print(arena._Stadium__name)
print(arena._Stadium__b)
arena._Stadium__print_capacity()
arena.set_name("Ice Hockey Stadium")
print(arena.get_name())