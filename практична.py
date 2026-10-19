products = {
    1: {"name": "Мишка", "price": 450.50, "stock": 10},
    2: {"name": "Клавіатура", "price": 850.00, "stock": 7},
    3: {"name": "Навушники", "price": 1200.99, "stock": 5},
    4: {"name": "Монітор", "price": 5500.00, "stock": 3}
}

cart = {}

item_total = lambda product_id, quantity: products[product_id]["price"] * quantity


def show_catalog():
    print("\n--- КАТАЛОГ ТОВАРІВ ---")
    for product_id, product in products.items():
        print(
            f"{product_id}. {product['name']} | "
            f"{product['price']:.2f} грн | "
            f"Залишок: {product['stock']} шт."
        )


def add_to_cart():
    show_catalog()

    try:
        product_id = int(input("Номер товару: "))
        quantity = int(input("Кількість: "))

        if product_id not in products:
            print("Такого товару немає.")
        elif quantity <= 0:
            print("Кількість має бути більшою за 0.")
        elif quantity > products[product_id]["stock"] - cart.get(product_id, 0):
            print("Недостатньо товару на складі.")
        else:
            cart[product_id] = cart.get(product_id, 0) + quantity
            print("Товар додано до кошика.")

    except ValueError:
        print("Введіть ціле число.")


def show_cart():
    print("\n--- КОШИК ---")

    if not cart:
        print("Кошик порожній.")
        return

    total = 0

    for product_id, quantity in cart.items():
        product = products[product_id]
        price = item_total(product_id, quantity)
        total += price
        print(f"{product['name']} x {quantity} = {price:.2f} грн")

    print(f"Загальна сума: {total:.2f} грн")


def remove_from_cart():
    show_cart()

    if not cart:
        return

    try:
        product_id = int(input("Номер товару для видалення: "))

        if product_id in cart:
            del cart[product_id]
            print("Товар видалено з кошика.")
        else:
            print("Товару немає в кошику.")

    except ValueError:
        print("Введіть ціле число.")


def buy_products():
    if not cart:
        print("Кошик порожній.")
        return

    total = sum(
        item_total(product_id, quantity)
        for product_id, quantity in cart.items()
    )

    for product_id, quantity in cart.items():
        products[product_id]["stock"] -= quantity

    cart.clear()
    print(f"Покупку здійснено! Сума: {total:.2f} грн")


def admin_login():
    login = input("Логін адміністратора: ")
    password = input("Пароль: ")

    if login == "admin" and password == "1234":
        print("\n--- ЗАЛИШКИ ТОВАРІВ ---")

        for product in products.values():
            print(f"{product['name']}: {product['stock']} шт.")
    else:
        print("Неправильний логін або пароль.")


def main():
    while True:
        print("\n===== МІНІМАГАЗИН =====")
        print("1. Переглянути каталог")
        print("2. Додати товар у кошик")
        print("3. Видалити товар із кошика")
        print("4. Переглянути кошик")
        print("5. Купити товари")
        print("6. Увійти як адміністратор")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            show_catalog()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            show_cart()
        elif choice == "5":
            buy_products()
        elif choice == "6":
            admin_login()
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірний пункт меню.")


if __name__ == "__main__":
    main()