import re

def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                split_info = [item.strip() for item in re.split(r'[,]+', line)] # Розділення рядка
                key = ['id', 'name', 'age']
                cat_info = dict(zip(key, split_info)) # Створення словника
                print(cat_info)
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
    except Exception as e:
        print(f"Помилка: {e}")

fun = get_cats_info('cats.txt')