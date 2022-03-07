a = 100
b = 345

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

if a > b: print("a is greater than b")

a = 250
b = 200
# Ternárny operátor
print("A") if a < b else print("B") 

print("A") if a > b else print("=") if a == b else print("B") if a < b else print("None")

print("A") if a > b else print("=") if a == b else print("B")


num = 20

if num % 2 == 0 and num % 3 == 0:
    print("That is it")


# If môžeme napísať aj do jedného riadku,
# ale vždy musíme napísať aj else časť
is_player = False
# is_player_string = "Is a player" if is_programmer
is_player_string = "He is a player" if is_player else "He is not a player"
print(is_player_string)

# Vieme prepísať do if - esle
if is_player:
    is_player_string ="He is a player"
else:
    is_player_string ="He is not a player"
print(is_player_string)
