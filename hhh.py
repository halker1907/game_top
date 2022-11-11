import random

first_name = ("жиран","дрын","брысь","жлык","пашок")
last_name = ("грозный","громкий","усатый","жирный","глупый")





def make_hero(name=None,hp=None,xp=None,attak=None,defence=None,money=None,potions=None):
    if not name:
        name=f"{random.choice(first_name)} {random.choice(last_name)}"
    if not hp:
        hp = random.randint(1,10)
    if not xp:
        xp = random.randint(0,10)
    if not attak:
        attak = random.randint(1,10)
    if not defence:
        defence = random.randint(0,10)
    if not money:
        money = random.randint(0,800)
    if not potions:
        potions = random.randint(0,0)
    return(name,hp,xp,attak,defence,money,potions)
player = make_hero()
enemy = make_hero()
enemy2 = make_hero()
enemy3 = make_hero()
enemy4 = make_hero()
enemy5 = make_hero()





def show_hero(hero:tuple):
    print("имя", hero[0])
    print("жизни", hero[1])
    print("опыт", hero[2])
    print("отака", hero[3])
    print("защита", hero[4])
    print("деньги", hero[5])
    print("зелья", hero[6])
    print("")