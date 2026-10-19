from tqdm import tqdm
import time

def show_progress():
    print("\nВиконання завдання:")
    for _ in tqdm(range(20)):
        time.sleep(0.02)
    print("Завершено!")
