import shop2
import hero
import os

def start_new_game():
	"""
	создает перса:
		имя
		здоровье
		деньги
		зелья

	"""
	#создаем перса
	print("запустили новую игру")
	player = ("безымянный", 100, 500, 0)

	is_game = True
	while is_game:
		os.system("cls")
		hero.show_player_stats(player)

		print("-- ситуация")
		print(f"{player[0]} приехал к камню")
		print("вирианты")
		print("1 поехать на битву")
		print("2 поехать играть в кости")
		print("3 поехать в лавку алхимика")
		print("0 ливнуть")
		


		answer = input("введите номер варианта и нажмите энтер ")
		if answer == "1":
			pass
		elif answer == "2":
			pass
		elif answer == "3":
			players = shop2.visit_shop(player)
		elif answer == "0":
			is_game = False


start_new_game()