"""Завдання 1

Потрібно розробити програму, яка імітує приймання й обробку заявок: програма має автоматично генерувати нові заявки 
(ідентифіковані унікальним номером або іншими даними), додавати їх до черги, а потім послідовно видаляти з черги для 
"обробки", імітуючи таким чином роботу сервісного центру."""

from queue import Queue
import time
import random

# Створюємо чергу заявок
requests_queue = Queue()

def generate_request():
    """
    Створює нову заявку з унікальним ідентифікатором і додає її до черги.
    """
    request_id = random.randint(1000, 9999)  # Генеруємо унікальний ID заявки
    print(f"Генеруємо нову заявку: {request_id}. Для зупунки натисніть Control+C")
    requests_queue.put(request_id)

def process_request():
    """
    Обробляє першу заявку в черзі, якщо черга не пуста.
    """
    if not requests_queue.empty():
        request_id = requests_queue.get()
        print(f"Обробляємо заявку: {request_id}")
    else:
        print("Черга пуста. Немає заявок для обробки.")

# Головний цикл програми
def main_loop():
    try:
        while True:
            generate_request()  # Генеруємо нову заявку
            time.sleep(1)  # Затримка для імітації часу надходження заявки
            process_request()  # Обробляємо заявку
    except KeyboardInterrupt:
        print("\nПрограма була перервана користувачем.")

# Викликаємо головний цикл програми
main_loop()