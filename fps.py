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
	weapon=None,
	shield=None,
	defence=0,
	money=None,
	level=1,
	luck=1,
	inventory=None
):
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

	if not weapon:
		weapon = {
			" тип": "оружие",
			" название": "меч обыкновенный",
			" цена": "+3",
			" модификатор": "5"
		}
	if not weapon:
		weapon = {
			" тип": "щит",
			" название": "щит обыкновенный",
			" цена": "+3",
			" модификатор": "5"
		}
	return {
		"имя": name,
		"хп сейчас": hp_now,
		"хп максимальное": hp_max,
		"опыт сейчас": xp_now,
		"опыт потом": xp_next,
		"сила аттаки": attak,
		"защита": defence,
		"оружие": weapon,
		"деньги": money,
		"уровень": level,
		"удача": luck,
		"инвентарь": inventory
	}

def show_item(item: dict) -> None:
	if item:
		print( f"{item['название']} {item['модификатор']}")
	else:
		print("-нет-")


def show_hero(hero):
	None


def fishing(hero, item):
	item = "рыбка"
	if hero["удача"] >= 1:
		hero["инвентарь"].append(item)
		print(f'{hero["имя"]} выловил рыбку из пруда')
	else:
		print(f'{hero["имя"]} не выловил рыбку')
	input("\nНажмите энтер")


def levelup(hero: list):
	while hero["опыт сейчас"] >= hero["опыт потом"]:
		hero["уровень"] += 1
		hero["опыт потом"] = hero["уровень"] * 100
		print(f'\n{hero["имя"]} получил {hero["уровень"]} уровень\n')


def buy(hero, price, item):
	os.system("cls")
	if hero["деньги"] >= price:
		hero["деньги"] -= price
		hero["инвентарь"].append(item)
		print(f'{hero["имя"]} купил {item} за {price} менет')
	else:
		print(f'у {hero["имя"]} нет столько монет')
	input("\nНажмите энтер")


def consume_item(hero: list):
	show_options(hero, hero["инвентарь"])
	index = choose_option(hero, hero["инвентарь"])
	if index is not None:
		if index <= len(hero["инвентарь"]) - 1 and index > -1:
			print("")
			print(f'{hero["имя"]} употрибил {hero["инвентарь"][index]}', end=", ")
			print("")
			if hero["инвентарь"][index] == "зелье здоровья":
				hero["хп сейчас"] += 10
				if hero["хп сейчас"] > hero["хп максимальное"]:
					hero["хп сейчас"] = hero["хп максимальное"]
				print(f'{hero["имя"]} восстановил здоровье')
				print("")

			elif hero["инвентарь"][index] == "зелье силы":
				if hero["сила аттаки"] >= 0:
					hero["сила аттаки"] += 6
				print("зелье вам прибавило урон на 6")

			elif hero["инвентарь"][index] == "зелье удачи":
				if hero["удача"] >= 0:
					hero["удача"] += 1
				print(f'{hero["имя"]} прибавилась удача на 1')
				print("")

			else:
				print("")
				print("у тебя никакого эфекта не проявилось")
				print("")
			hero["инвентарь"].pop(index)
		else:
			print("нет такого предмета")


def play_dice(hero, bet):
	try:
		bet = int(bet)
	except ValueError:
		print("ошибка, ставка должна быть написана цифрой")
	else:
		if bet > 0:
			if hero["деньги"] >= bet:
				hero_score = randint(2, 12)
				casino_score = randint(2, 12)
				print(f'{hero["имя"]} выбросил кубики и выпало {hero_score}')
				print(f" трактирщик выбросил кубики и выпало {casino_score}")
				if hero_score > casino_score:
					hero["деньги"] += bet
					print(f'{hero["имя"]} выиграл {bet}')
				elif hero_score < casino_score:
					hero["деньги"] -= bet
					print(f'{hero["имя"]} проиграл {bet}')
				else:
					print("ничья ")
			else:
				print(f'у {hero["имя"]} нет столько денег')
		else:
			print("такая ставка невозможна,стаки начинаются от одной монеты!")
	input("нажмите энтер чтобы продолжить")


def combat_turn(attacker, defender):
	if attacker["хп сейчас"] > 0:
		damage = attacker["сила аттаки"]
		defender["хп сейчас"] -= damage
		print(f'{attacker["имя"]} ударил {defender["имя"]} на {damage} урон')


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
	enemy = make_hero(hp_now=10, money=100, xp_now=50, inventory=["меч", "щит"])
	options = [
		"ударить врага",
		"использовать предмет",
	]
	show_hero(hero)
	print("")
	show_hero(enemy)

	while hero["хп сейчас"] > 0 and enemy["хп сейчас"] > 0:
		show_options(hero, options)
		option = choose_option(hero, options)
		os.system("cls")
		if option == 0:
			combat_turn(hero, enemy)
			combat_turn(enemy, hero)
			show_hero(hero)
			print("")
			show_hero(enemy)
		elif option == 1:
			consume_item(hero)
			show_hero(hero)
			print("")
			show_hero(enemy)
			combat_turn(enemy, hero)
	combat_result(hero, enemy)
	input("\nнажмите энтер чтобы продолжить")
	return visit_arena(hero)


def combat_result(hero, enemy):
	os.system("cls")
	if hero["хп сейчас"] > 0 and enemy["хп сейчас"] <= 0:
		print(f'{hero["имя"]} победил и в награду получает')
		print(enemy["опыт сейчас"], "опыта")
		hero["опыт сейчас"] += enemy["опыт сейчас"]
		print(enemy["деньги"], "денег")
		hero["деньги"] += enemy["деньги"]
		print("и забирает все предметы: ", end="")
		for item in enemy["инвентарь"]:
			print(item, end=", ")
		hero["инвентарь"] += enemy["инвентарь"]
		levelup(hero)
	elif  hero["хп сейчас"] <= 0 and enemy["хп сейчас"] > 0:
		print(f'{enemy["имя"]} победил')
	else:
		print(f'{hero["имя"]} и {enemy["имя"]} пали в бою')
	input("\nнажмите энтер для продолжения")


def show_options(hero, options):
	for num, option in enumerate(options):
		print(f"{num}. {option}")


def choose_option(hero, options):
	"""
	описание ситуации где происходит выбор
	принимает список возможных вариантов
	спросить пользователя номер варианта
	проверяет есть ли вариант пользователя в возможных вариантах 
	если есть возвращает вариант пользователя
	"""

	option = input("\nВведите номер варианта и нажмите энтер: ")
	try:
		option = int(option)
	except ValueError:
		print("ошибка! введите целое неотрицательное число")
	else:
		if option < len(options) and option > -1:
			return option
		else:
			print("такой выбор невозможен")


def visit_hub(hero):
	text = f'{hero["имя"]} приехал в хаб отсюда идут несколько дорог'
	options = [
		"купить зелье ",
		"сыграть в кости на ставку",
		"поехать на арену",
		"съездить на рыбалку"
	]
	os.system("cls")
	show_hero(hero)
	print("")
	print(text)
	show_options(hero, options)
	option = choose_option(hero, options)
	os.system("cls")
	if option == 0:
		return visit_shop(hero)
	elif option == 1:
		return visit_inn(hero)
	elif option == 2:
		return visit_arena(hero)
	elif option == 3:
		return visit_fishing(hero)
	else:
		print("нет такого варианта")
	input("\n нажмите энтер для продолжения")


def visit_shop(hero):
	"""
	
	"""
	text = f'{hero["имя"]} приехал в лавку алхимика здесь продаются зелья и странно пaхнет'
	options = [
		"зелье здаровья за 10 монет ",
		"зелье силы 20 монет ",
		"зелье опыта 20 монет ",
		"уйти в хаб ",
	]
	os.system("cls")
	show_hero(hero)
	print("")
	print(text)
	show_options(hero, options)
	option = choose_option(hero, options)
	os.system("cls")
	if option == 0:
		buy(hero, 10, "зелье здоровья")
		return visit_shop(hero)
	elif option == 1:
		buy(hero, 20, "зелье силы")
		return visit_shop(hero)
	elif option == 2:
		buy(hero, 20, "зелье опыта")
		return visit_shop(hero)
	elif option == 3:
		return visit_hub(hero)
	else:
		print("нет такого варианта")
		input("\n нажмите энтер для продолжения")
		return visit_shop(hero)


def visit_inn(hero):
	text = f'{hero["имя"]} приехал в таверну он может сыграть на ставку'
	options = [
		"начать играть ",
		"уйти в хаб",
	]
	os.system("cls")
	show_hero(hero)
	print("")
	print(text)
	show_options(hero, options)
	option = choose_option(hero, options)
	os.system("cls")
	if option == 0:
		show_hero(hero)
		bet = input("\nвведите сколько монет поставить и нажмите энтер: ")
		play_dice(hero, bet)
	elif option == 1:
		return visit_hub(hero)
	else:
		print("нет такого варианта")
	return visit_inn(hero)


def visit_arena(hero):
	text = f'{hero["имя"]} приехал на арену, он может сразиться и забрать ресы врага'
	options = [
		"начать сражаться ",
		"уйти в хаб",
	]
	os.system("cls")
	show_hero(hero)
	print("")
	print(text)
	show_options(hero, options)
	option = choose_option(hero, options)
	os.system("cls")
	if option == 0:
		fight(hero)
		return visit_arena(hero)
	elif option == 1:
		return visit_hub(hero)
	else:
		print("нет такого варианта")
		input("\n нажмите энтер для продолжения")
		return visit_arena(hero)


def visit_fishing(hero):
	item = "рыбка"
	text = f'{hero["имя"]} приехал на пруд, он может порыбачить и забрать рыбку себе'
	options = [
		"начать рыбачить ",
		"уйти в хаб",
	]
	os.system("cls")
	show_hero(hero)
	print("")
	print(text)
	show_options(hero, options)
	option = choose_option(hero, options)
	os.system("cls")
	if option == 0:
		fishing(hero, item)
		return visit_fishing(hero)
	elif option == 1:
		return visit_hub(hero)
	else:
		print("нет такого варианта")
		input("\n нажмите энтер для продолжения")
		return visit_fishing(hero)