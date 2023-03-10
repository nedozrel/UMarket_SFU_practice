import UMarket as app


def main():
	cart = app.Cart()

	while True:
		choice = int(input("""
	1. Добавить продукты в корзину
	2. Удалить продукты из корзины
	3. Посмотреть корзину
	4. Сбалансировать корзину
	5. Выход
	"""))
		if choice == 5:
			break

		if choice == 1:
			while True:
				output = "Выберите категорию: \n"
				index = 0
				for index, category in enumerate(app.categories.categories_list):
					output += f"{index}. {category}\n"
				output += f"{index + 1}. Вернуться в меню\n"
				category_choice = int(input(output))
				if category_choice == index + 1:
					break
				category = app.categories.categories_list[category_choice]
				products = app.AllProducts.get_products_by_category(category)

				while True:
					output = "Выберите продукт: \n"
					index = 0
					for index, product in enumerate(products):
						output += f"{index}. {product}\n"
					output += f"{index + 1}. Вернуться к выбору категории\n"
					product_choice = int(input(output))
					if product_choice == index + 1:
						break
					product = products[product_choice]
					cart.add(product)
		if choice == 2:
			print(cart)
			delete_choice = input("Напишите название продукта для удаления: ")
			product_to_delete = app.AllProducts.get_product_by_name(delete_choice)
			if product_to_delete is None:
				print("Неверное имя продукта!")
			else:
				cart.remove_product(product_to_delete)
				print("Продукт успешно удален!")
		if choice == 3:
			print(cart)
		if choice == 4:
			cart.balance()
		if choice == 5:
			break


if __name__ == '__main__':
	main()
