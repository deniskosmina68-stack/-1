from tabulate import tabulate

def show_table():
    data = [
        ["Мишка", "450.50 грн"],
        ["Клавіатура", "850.00 грн"],
        ["Навушники", "1200.99 грн"]
    ]
    print("\n--- Таблиця товарів ---")
    print(tabulate(data, headers=["Товар", "Ціна"], tablefmt="grid"))
