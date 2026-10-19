from faker import Faker

fake = Faker()

def generate_user():
    print("\n--- Випадковий користувач ---")
    print("Ім'я:", fake.name())
    print("Місто:", fake.city())
    print("Email:", fake.email())
