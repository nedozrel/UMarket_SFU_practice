from UMarket.thing import Thing
import UMarket.categories as categories
import UMarket.food as food
import UMarket.nutrients as nutrients
from UMarket.categories import Category


class AllProducts:
	pen = Thing("Ручка")
	notebook = Thing("Блокнот")
	chocolate_bar = food.Food(
		"Шоколадка",
		categories.snacks,
		nutrients.carbohydrates
	)
	crisps = food.Food(
		"Чипсы",
		categories.snacks,
		nutrients.fats
	)
	balyk_cheese = food.Food(
		"Сыр балык",
		categories.snacks,
		nutrients.proteins
	)
	chicken = food.Food(
		"Курица",
		categories.healthy_food,
		nutrients.proteins
	)
	olive_oil = food.Food(
		"Оливковое масло",
		categories.healthy_food,
		nutrients.fats
	)
	fruit = food.Food(
		"Фрукты",
		categories.healthy_food,
		nutrients.carbohydrates
	)
	dumpling_meat = food.Food(
		"Пельмени",
		categories.semi_finished_food,
		nutrients.proteins
	)
	cheburek = food.Food(
		"Чебурек",
		categories.semi_finished_food,
		nutrients.fats
	)
	dumpling_berries = food.Food(
		"Вареники с ягодами",
		categories.semi_finished_food,
		nutrients.carbohydrates
	)

	@classmethod
	def get_products_by_category(cls, category: Category):
		products_list = []
		for product in cls.get_dict().values():
			if isinstance(product, food.Food):
				if product.category == category:
					products_list.append(product)
		return products_list

	@classmethod
	def get_product_by_name(cls, name: str):
		for product in cls.get_dict().values():
			if isinstance(product, (Thing, food.Food)):
				if product.name.lower() == name.lower():
					return product
		return None

	@classmethod
	def get_dict(cls):
		return cls.__dict__
