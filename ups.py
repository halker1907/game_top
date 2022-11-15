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
	
	"""
	print("имя", hero[0])
    print("жизни сейчас и потом", hero[1])
    print("жизни потом", hero[2])
	print("опыт сейчас и потом", hero[3])
    print("опыт потом", hero[4])
    print("атака сила", hero[5])
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
		luck,
	]


def show_hero(hero):
	print("имя", hero[0])
    print("жизни сейчас", hero[1])
    print("жизни потом", hero[2])
	print("опыт сейчас", hero[3], "/", hero[4])
    print("опыт потом", hero[4])
    print("атака сила", hero[5])
    print("защита", hero[6])
    print("деньги", hero[7])
    print("левел", hero[8])
    print("удача", hero[9])
    print("")

p1 = make_hero()
show_hero(p1)
p2 = make_hero()
show_hero(p2)
p3 = make_hero()
show_hero(p3)

show_hero()
show_hero()
show_hero()