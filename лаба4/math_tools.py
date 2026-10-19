import math
import random

def calculate():
    number = random.randint(1, 100)
    print("\nВипадкове число:", number)
    print("Квадратний корінь:", round(math.sqrt(number), 2))
