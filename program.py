import time
from db import DBManager
from scrap import Scrapper


class Date:
    def __str__(self):
        return str(time.strftime("%Y-%m-%d %H:%M"))


if __name__ == "__main__":
    db_manager = DBManager()
    db_manager.create_tables()

    # Отримуємо посилання від користувача
    url = input("Введіть посилання на товар з одного з магазинів: ")

    # Створюємо об'єкт Scrapper для скрапінгу даних
    scrapper = Scrapper(url)

    # Встановлюємо час збирання даних
    date_scraped = Date()

    # Збираємо інформацію про товар
    product_name = scrapper.get_product_name()
    price = scrapper.get_price()
    store = scrapper.get_store()

    # Зберігаємо в базу даних
    db_manager.insert_data(store, product_name, price, str(date_scraped))  # Перетворюємо Date в рядок

    # Закриваємо з'єднання з базою
    db_manager.close()
