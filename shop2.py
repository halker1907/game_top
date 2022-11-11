import os
import hhh

def visit_shop(player):
	os.system("cls")
	print(f"{player[0]} приехал в магазин")

	hhh.make_hero(player)
	print("деньги:", hero[5])
	print("зелья:", hero[6])

	print("1 - купить зелье")
	print("2 - уехать к камню")

		
	answer = input("введите номер дороги и нажмите энтер")

	if answer == "1":
		if hero[6] >= 200:
			hero[6] -= 200
			hero[6] += 1
			print(f"{player[0]} купил зелье")
		else:
			print ("у вас нет столько деняк")
			input("нажмите энтер для продолжения")
	elif answer == "2":
		return player
