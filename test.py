from fps import*

player = make_hero(
	name="вася",
	inventory=[
		{
			" тип": "щит",
			" название": "меч кладенец",
			" цена": "500",
			" модификатор": "50"
		} 
	]
	)		
game = True
while game:
	visit_hub(player)