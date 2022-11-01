import os
import hero

def visit_shop(player):
	os.system("cls")
	print(f"{player[0]} приехал в магазин")

	hero.show_player_stats(player)
	print(f"здоровье:",player[1])
	print(f"деньги:",player[2])
	print(f"зелья:",player[3])

	print("1 - купить зелье")
	print("2 - уехать к камню")

		
	answer = input("введите номер дороги и нажмите энтер")

	if answer == "1":
		if player[2] >= 200:
			player[2] -= 200
			player[2] += 1
			print(f"{player[0]} купил зелье")
		else:
			print ("у вас нет столько денег")
			input("нажмите энтер для продолжения")
	elif answer == "2":
		return player


