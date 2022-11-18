from random import choice,randint

first_name = ("жиран","дрын","брысь","жлык","крикун")
last_name = ("грозный","громкий","усатый","жирный","глупый")

def make_hero(
	name=None,
	hp_now=None,
	xp_now=0,
	xp_next=1000,
	attak=1,
	defence=0,
	money=None,
	level=1,
	luck=1,
	inventory=None
):
	
	"""hero[0])
    print("жизни 
	print("имя", сейчас и потом", hero[1])
    print("жизни потом", hero[2])
	print("опыт сетом", hero[4])
    print("атака сйчас и потом", hero[3])
    print("опыт поила", hero[5])
    print("защита", hero[6)
    print("деньги", hero[7])
    print("зелья", hero[8])
    luck удача [9]
    level левел [10]


    """
	if not name:
		name = choice(first_name) + " " + choice(last_name)
	if not inventory:
		inventory = []
	if not hp_now:
		hp_now = randint(1,10)
		hp_max = hp_now
	if money is None:
		money = randint(0,100)

	return [
		name,
		hp_now,
		xp_now,
		xp_next,
		attak,
		defence,
		money,
		level,
		luck
	]


def show_hero(hero):
	print("имя", hero[0])
	print("жизни ", hero[1], "из", hero[2])
	print("опыт сейчас", hero[3], "/", hero[4])
	print("атака сила", hero[5])
	print("защита", hero[6])
	print("деньги", hero[7])
	print("левел", hero[8])
	print("удача", hero[9])
	print("инвентарь", hero[10])
	print("")


def levelup(hero: list):
	if hero[4] >= hero[5]:
		hero[3] += 1
		hero[5] = hero[3] * 100
		print(f"{hero[0]} получил {hero[3]} уровень\n")


def buy(hero, price):
	"""
	[9] money - деньги
	[10] inventory - cписок предметов
"""
	if hero[7] >= price:
		hero[7] -= price
		hero[10].append("зелья")
		print(f"{hero[0]} купил зелье за {price} менет")
	else:
		print(f"у {hero[0]} нет столько монет")

def consume_item(hero: list, item: str):



p1 = make_hero()
p2 = make_hero()
show_hero(p1)
show_hero(p2)
