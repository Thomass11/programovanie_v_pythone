# Statická metóda
class Player:

    class_my_variable = "NHL"
    
    def __init__(self, name_p,  age):
        self.name = name_p
        self.age = age

    
    # Static metóda
    @staticmethod
    def get_points(goals, assists):
        return goals + assists

p1 = Player.get_points(25, 42)
print(p1)


# Dedenie
class Person:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.surname = last_name

    def show_person(self):
        print(f"Person: {self.name} {self.surname}")

class Player(Person):
    def __init__(self, first_name, last_name, number):
        # Môžme vynechať
        # Person.__init__(self, first_name, last_name)
        super().__init__(first_name, last_name)
        # self.name = first_name
        # self.surname = last_name
        self.number = number
    
    def show_person(self):
        # Dedí správanie z triedy Person
        super().show_person()
        print(f"Number: {self.number}")

p2 = Player("Marian", "Hossa", 81)
p2.show_person()


# Viacúrovňové dedenie

class Person:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.surname = last_name

    def show_person(self):
        print(f"Person: {self.name} {self.surname}")


class Player(Person):
    def __init__(self, first_name, last_name, number):
        super().__init__(first_name, last_name)
        self.number = number
    
    def show_person(self):
        super().show_person()
        print(f"Number: {self.number}")

class Trainer(Player):
    pass

p1 = Person("Tomas", "Tatar")
p2 = Player("Marian", "Hossa", 81)
t1 = Trainer("Joe", "Quenneville", 1)
t1.show_person()

print(isinstance(p2, Person))
print(isinstance(p2, Player))
print(isinstance(p1, Player))
print(isinstance(t1, Person))

print(issubclass(Player, Person))
print(issubclass(Person, Player))
