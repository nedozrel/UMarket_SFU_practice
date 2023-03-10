
class Category:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name


snacks = Category("Снэки")
healthy_food = Category("Здоровая пища")
semi_finished_food = Category("Полуфабрикаты")

categories_list = [
	snacks,
	healthy_food,
	semi_finished_food
]