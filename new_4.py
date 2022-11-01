import os
import game


def show_menu():
	"""
	печатает на экране главного меню 
	умеет запускать игру 
	умеет выходить из программы
	выборы:
		начать новую игру
		настройки
		загрузка старой	 игры
		выход
	"""
	while True:
		os.system("cls")
		print("вриант выбири")
		print("1 - начать новую игру 2 - выйти из игры ")
		print("2- выйти из игры ")

		answer = input("введите ответ и нажмите энтер ")
		if answer == "1":
			game.start_new_game()
		elif answer == "0":
			print("вышли из игры ")
			break

show_menu()