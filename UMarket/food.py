from UMarket.thing import Thing
from UMarket.nutrients import Nutrient
from UMarket.categories import Category


class Food(Thing):
	def __init__(self, name, category: Category, nutrient: Nutrient):
		super().__init__(name)
		if isinstance(category, Category):
			self.category: Category = category
		else:
			raise TypeError

		if isinstance(nutrient, Nutrient):
			self.nutrient: Nutrient = nutrient
		else:
			raise TypeError

	def __repr__(self):
		return self.name
