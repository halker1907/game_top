import os
from random import choice,randint

first_name = ("жиран","дрын","брысь","жлык","крикун")
last_name = ("грозный","громкий","усатый","жирный","глупый")


def make_hero(
	name=None,
	hp_now=None,
	hp_max=None,
	xp_now=10,
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
	if not hp_max:
		hp_max = hp_now
	if money is None:
		money = randint(0,100)

	return [
		name,
		hp_now,
		hp_max,
		xp_now,
		xp_next,
		attak,
		defence,
		money,
		level,
		luck,
		inventory
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
	while hero[3] >= hero[4]:
		hero[8] += 1
		hero[4] = hero[8] * 100
		print(f"{hero[0]} получил {hero[8]} уровень\n")


def buy(hero, price,item):
	if hero[7] >= price:
		hero[7] -= price
		hero[10].append(item)
		print(f"{hero[0]} купил {item} за {price} менет")
	else:
		print(f"у {hero[0]} нет столько монет")


def consume_item(hero: list, index: str):
	if index <= len(hero[10]) - 1 and index > -1:
		print(f"{hero[0]} употрибил {hero[10][index]}")
		if hero[10][index] == "зелье":
			hero[1] += 10
			if hero[1] > hero[2]:
				hero[1] = hero[2]
		elif hero[10][index] == "яблоко":
			pass
		else:
			print("никокого эфекта")
		hero[10].pop(index)
	else:
		print("нет такого предмета")


def play_dice(hero, bet):
	if bet > 0:
		if hero[7] >= bet:
			hero_score = randint(2, 12)
			casino_score = randint(2, 12)
			print(f"{hero[0]} выбросил кубики и выпало {hero_score}")
			print(f" трактирщик выбросил кубики и выпало {casino_score}")
			if hero_score > casino_score:
				hero[7] += bet
				print(f"{hero[0]} выиграл {bet}")
			elif hero_score < casino_score:
				hero[7] -= bet
				print(f"{hero[0]} проиграл {bet}")
			else:
				print("ничья ")
		else:
			print(f"у {hero[0]} нет столько денег")
	else:
		print("такая ставка невозможна,стаки начинаются от одной монеты!")

def combat_turn(attacker,defender):
	if attacker[1] > 0:
		damage = attacker[5]
		defender[1] -= damage
		print(f"{attacker[0]} ударил {defender[0]} на {damage} урона")
		os.system("cls")

def fight(hero):
	"""
	Cделать врага 
	Зависит ли враг от уровня героя
	обмен ударами пока у всех есть жизни
	формула атаки и защита
	После боя забрать опыт деньги и предметы
	Проверить лэвел ап
	Можно ли выпить зелье в бою?

	"""
	enemy = make_hero(money=100, xp_now=50000, inventory=("меч", "щит"))
	while hero[1] > 0 and enemy[1] > 0:
		os.system("cls")
		combat_turn(hero,enemy)
		combat_turn(enemy,hero)
		print("")
		show_hero(hero)
		show_hero(enemy)
		input("\nНажмите энтер чтобы сделать следующий ход")
	combat_result(hero, enemy)
	os.system("cls")


def combat_result(hero, enemy):
	os.system("cls")
	if hero[1] > 0 and enemy[1] <= 0:
		print(f"{hero[0]} победил и в награду получает")
		print(enemy[3], "опыта")
		hero[3] += enemy[3]
		print(enemy[7], "денег")
		hero[7] += enemy[7]
		print("и забирает все предметы ", end="")
		for item in enemy[10]:
			print(item, end=", ")
		hero[10] += enemy[10]
		levelup(hero)
	elif  hero[1] <= 0 and enemy[1] > 0:
		print(f"{enemy[0]} победил")
	else:
		print(f"{hero[0]} и {enemy[0]} пали в бою")
