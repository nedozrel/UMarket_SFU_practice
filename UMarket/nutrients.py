
class Nutrient:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name


fats = Nutrient("Fat")
carbohydrates = Nutrient("Carbohydrates")
proteins = Nutrient("Protein")

nutrients_frozenset = frozenset([fats, carbohydrates, proteins])