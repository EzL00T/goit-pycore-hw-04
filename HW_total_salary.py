import re

with open('salary.txt', 'w', encoding='utf-8') as f:
    f.write('Alex Korp,3000 \nNikita Borisenko,2000 \nSitarama Raju,1000')
    

def total_salary(path):
    try: 
        with open(path, 'r', encoding='utf-8') as f:
            all_salaries = []
            for file in f:
                find_salary = re.findall(r'\d+', file) # регулярний вираз для пошуку чисел
                all_salaries.extend(find_salary) # додавання знайдених зарплат до списку
            salaries = list(map(float, all_salaries)) # перетворення рядків у числа
            num_people = len(salaries) # кількість людей
            sum_salaries = sum(salaries) # сума зарплат
        return sum_salaries, sum_salaries / num_people # повернення суми та середньої зарплати
    except FileNotFoundError:
        print("Файл відсутній або пошкоджений.")
        return 0, 0
    except Exception as e:
        print(e)
        return 0, 0

salary = total_salary('salary.txt')
print(f'Загальна сума заробітної плати: {salary[0]}$ та середня заробітна плата: {salary[1]}$')