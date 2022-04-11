# Class variable

class Player:

    # Class premenná
    class_my_variable = "NHL"

    def __init__(self, name_p, surname_p, number):
        self.name = name_p
        self.surname = surname_p
        self.number = number

    def show_player(self):
        print(f"Player: {self.name} {self.surname} {self.number}")


p1 = Player("Tomas", "Tatar", 21)
p1.show_player()
p2 = Player.class_my_variable
print(p2)


# Class method
from datetime import date
class Player:

    class_my_variable = "NHL"
    
    def __init__(self, name_p, age):
        self.name = name_p
        self.age = age
 
    # Class metóda
    @classmethod
    def get_age(cls, name, year): 
        return cls(name, date.today().year - year)   

p1 = Player.get_age("Brent Seabrook",1991)
print(p1.name)
print(p1.age)
