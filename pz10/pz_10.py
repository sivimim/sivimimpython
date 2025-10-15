«В озере водится несколько видов рыб. Три рыбака поймали рыб некоторых их имеющихся в озере видов. Определить, рыб каких видов поймал каждый рыбак и рыб каких видов, имеющихся в озере, не выловил ни один из рыбаков.»

import random

fish_types = {"Карась","Щука", "Карп", "Сазан", "Красноперка"}

fisher_man_1 = fish_types.copy()
fisher_man_2 = fish_types.copy()
fisher_man_3 = fish_types.copy()

def fishing(man_1, man_2, man_3):
    rnd_pop_amount_1 = random.randint(2,4)
    rnd_pop_amount_2 = random.randint(2,4)
    rnd_pop_amount_3 = random.randint(2,4)

    for i in range(rnd_pop_amount_1):
        man_1.pop()
    for i in range(rnd_pop_amount_2):
        man_2.pop()
    for i in range(rnd_pop_amount_3):
        man_3.pop()

    return man_1, man_2, man_3


fisher_man_1, fisher_man_2, fisher_man_3 = fishing(fisher_man_1, fisher_man_2, fisher_man_3)

print("Улов первого рыбака:", fisher_man_1)
print("Улов второго рыбака:", fisher_man_2)
print("Улов третьего рыбака:", fisher_man_3)
