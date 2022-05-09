# Abstrakcia

from abc import ABC, abstractmethod

# Abstraktná trieda
class Stadium(ABC):

    @abstractmethod # abstraktná metóda
    def __init__(self, address):
        pass
   
    @abstractmethod # abstraktná metóda
    def play_horn(self):
        pass

    def show_info(self):
        print("NHL Game")
    
    @property
    @abstractmethod # abstraktná premenná, getter
    def address(self):
        pass

    @address.setter # abstraktná premenná, setter
    @abstractmethod
    def address(self, value):
        pass

class HockeyStadium(Stadium):
    # Použitím len parametra self s pass argumentom v tele 
    # obídeme konštruktor z abstraktnej triedy
    def __init__(self, address, capacity):
        self.address = address
        self.capacity = capacity
    
    def play_horn(self): # povinná metóda
        pass

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        print("Address set")
        self._address = value

    @property
    def capacity(self):
        return self._capacity # povinná premenná

    @capacity.setter
    def capacity(self, value):
        print("Capacity set")
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0")
        self._capacity = value

h_stadium_1 = HockeyStadium("1901 West Madison Street, Chicago", 17000)
print(h_stadium_1.address)

h_stadium_1.capacity = 1800
print(h_stadium_1.capacity)

# Metóda z abstraktnej triedy, ktorá nie je abstraktná
# voláme z objektu zdedenej triedy
h_stadium_1.show_info()