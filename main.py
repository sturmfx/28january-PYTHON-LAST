import random
import math
a = 1
b = 100
number = random.randint(a, b)
allowed_g = math.ceil(math.log2(b-a))
g_made = 0
while True:
    player_g = int(input(" Угадай число от {} до {}".format(a, b)))
    if (player_g < a) or (player_g > b):
        print("Совсем не те числа!")
        print("Загаданное число - {}".format(number))
        break
    g_made = g_made + 1
    if player_g == number:
        print("Ты офигенный везунчик и угадал за {} попыток".format(g_made))
        break
    elif player_g < number:
        print("Слишком мало!!!")
    else:
        print("Слишком много!!!")
    if g_made == allowed_g:
        print("Ты неудачник и использовал все попытки!GG")
        print("Загаданное число - {}".format(number))
        break
    else:
        print("Осталось {} попыток!".format(allowed_g - g_made))
