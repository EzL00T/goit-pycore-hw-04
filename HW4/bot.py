contacts = {}

def add_contact(name, phone): # Функція для додавання контакту
    contacts[name] = phone
    return f"Додано контакт {name} з телефоном {phone}"

def change_contact(name, phone): # Функція для зміни контакту
    if name in contacts:
        contacts[name] = phone
        return f"Оновлено контакт {name} з новим телефоном {phone}"
    else:
        return f"Контакт {name} не знайдено"

def show_phone(name): # Функція для показу телефону контакту
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return f"Контакт {name} не знайдено"

def show_all(): # Функція для показу всіх контактів
    if not contacts:
        return "Контакти не збережено"
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def parse_input(user_input): # Функція для обробки введення користувача
    parts = user_input.lower().split()
    if not parts:
        return "Введіть команду"
    
    command = parts[0] 

    if command == "привіт": 
        return "Як я можу вам допомогти?"
    elif command == "додати" and len(parts) == 3:
        return add_contact(parts[1], parts[2])
    elif command == "змінити" and len(parts) == 3:
        return change_contact(parts[1], parts[2])
    elif command == "телефон" and len(parts) == 2:
        return show_phone(parts[1])
    elif command == "всі":
        return show_all()
    elif command == "help":
        return (
        "Доступні команди:\n"
        "привіт — Привітання\n"
        "додати [ім'я] [номер] — Додати контакт\n"
        "змінити [ім'я] [номер] — Змінити контакт\n"
        "телефон [ім'я] — Показати номер\n"
        "всі — Показати всі контакти\n"
        "вихід / закрити — Завершити роботу\n"
        "help — Показати цю допомогу"
    )
    elif command in ["вихід", "закрити"]:
        return "До побачення!"
    else:
        return "Невідома команда. Спробуйте ще раз."


def main(): # Головна функція для запуску бота
    while True:
        user_input = input("Введіть команду: ")
        result = parse_input(user_input)
        print(result)
        if result == "До побачення!":
            break

if __name__ == "__main__":
    main()
