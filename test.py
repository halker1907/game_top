from ups import*

player = make_hero(name="вася", inventory=["зелье", "зелье здоровья", "зелье силы"], hp_now=40)
game = True
while game:
	visit_hub(player)