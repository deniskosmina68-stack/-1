import orjson
from faker import Faker
from datetime import datetime

fake = Faker()

def create_json():
    data = {
        "name": fake.name(),
        "city": fake.city(),
        "date": datetime.now().strftime("%d.%m.%Y")
    }
    with open("user.json", "wb") as file:
        file.write(orjson.dumps(data, option=orjson.OPT_INDENT_2))
    print("\nДані збережено у файлі user.json")
