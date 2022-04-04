# Prvý príklad
try:
    a = "Patrick Kane"
    b = 10
    a + b
# Zachytíme chybu z try časti
except TypeError as error:
    print(f"TypeError: {error}")
# finally blok sa vykoná, bez ohľadu na (ne)vyskytnutie chyby v try časti
finally:
    print("Toto sa spusti bez ohladu na chybu/nechybu")

print("Spustenie dalsich prikazov...")


# Druhý príklad
result = None

while True:
    try:
        age = input('Vloz svoj vek: ')
        age = int(age)
        print(f"Tvoj vek je {age}")
        break
    except ValueError:
        print(f"Vek nie je cislo")


# Tretí príklad
age = input("Vloz svoj vek: ")
age = int(age)
try:
    if age < 18:
        raise Exception("Si neplnolety", "Nemas narok na vstup", f"Musis pockat {18 - age} rokov")
except Exception as e:
    # Vieme pristúpiť k položke tuple
    print(f"{e.args[2]}")
    print(f"{e}")


# Štvrtý príklad
# Definujeme vlastné výnimky
class IncorrectValueException(Exception):

    def __init__(self, msg):
        self.msg = msg

    def message(self):
        return self.msg

class LargeValueException(Exception):

    def __init__(self, msg):
        self.msg = msg

    def message(self):
        return self.msg


class SmallValueException(Exception):

    def __init__(self, msg):
        self.msg = msg

    def message(self):
        return self.msg


value = 10

try:
    if not(isinstance(value, int)):
        raise InCorrectValueExcpetion("Hodnota nie je integer")
    elif value > 100:
        raise LargeValueException("Hodnota je vacsia ako 100")
    elif value < 0:
        raise SmallValueException("Hodnota je mensia ako 0")
    print(f"Hodnota je medzi 0 - 100 ({value})")
except InCorrectValueExcpetion as incorrect:
    print(f"{incorrect.message}")
except LargeValueException as large:
    print(f"{large.message()}")
except SmallValueException as small:
    print(f"{small.message()}")

print(f"Aplikacia ukonci beh")
