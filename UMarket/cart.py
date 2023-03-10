from UMarket.food import Food
import UMarket.categories as categories
import UMarket.nutrients as nutrients
from UMarket.all_products import AllProducts


def type_food_check(method):
	def wrapper(self, obj):
		if isinstance(obj, Food):
			method(self, obj)
		else:
			raise TypeError()
	return wrapper


class Cart:
	def __init__(self):
		self.products: dict[Food, int] = {}
		self.nutrients_set: set[nutrients.Nutrient] = set()
		self.categories_set: set[categories.Category] = set()

	@type_food_check
	def add(self, product: Food):
		self.nutrients_set.add(product.nutrient)
		self.categories_set.add(product.category)
		if self.products.get(product):
			self.products[product] += 1
		else:
			self.products[product] = 1

	@type_food_check
	def remove_product(self, product: Food):
		product_amount = self.products.get(product)
		if product_amount > 1:
			self.products[product] -= 1
		elif product_amount is None:
			print("Такого продукта в корзине нет!")
		elif product_amount <= 1:
			del self.products[product]
		else:
			print("Какая то дичь")

	def balance(self):
		if not self.categories_set:
			print("Корзина пуста, невозможно сбалансировать")
			return

		nutrients_needed = nutrients.nutrients_frozenset - self.nutrients_set
		chosen_categories_list = list(self.categories_set)
		chosen_categories_sorted = sorted(chosen_categories_list, key=lambda x: x.name)
		if len(self.categories_set) > 1:
			choose_category_string = "Категория для балансировки: \n"
			for index, category in enumerate(chosen_categories_sorted):
				choose_category_string += f"{index}. {category} \n"
			choice = int(input(choose_category_string))
			category_for_search = chosen_categories_sorted[choice]
		else:
			category_for_search = self.categories_set.copy().pop()

		products_from_chosen_category = []

		for i in AllProducts.get_dict().values():
			if isinstance(i, Food):
				if i.category == category_for_search:
					products_from_chosen_category.append(i)

		for product in products_from_chosen_category:
			if product.nutrient in nutrients_needed:
				self.add(product)

		print("Корзина успешно сбалансирована!\n")

	def __repr__(self):
		output = ""
		counter = 1
		for key, value in self.products.items():
			output += f"{counter}. {key} - {value} шт.\n"
			counter += 1
		if not output:
			output = "Корзина пуста!"
		return output

