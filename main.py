# Ссылочка на гит, если надо - https://github.com/andrey-seredinin/external-multiway-merge-sort

import random
import heapq

# Получаем от пользователя файл куда записать все результаты
output_file = input('Введите название файла для слияния в него результатов программы ')

# Определяем файлы уже созданы пользователем или нам нужно создать самим
info = input('Здравствуйте файлы для сортировки создаем новые? (y/n) ')
file_names = []
if info == 'y':
    count = int(input('Сколько файлов создаем? '))
    if 1 < count < 11:

        def generate_files(count_files, min_count=1, max_count=999, num_values=10):
            """Функция создает количество файлов указанных пользователем с 10 числами"""
            for i in range(count_files):
                with open(f'{i}_exemple.txt', 'w') as f:
                    for j in range(num_values):
                        count_write = str(random.randint(min_count, max_count))
                        # С новой строки записываем числа
                        f.write(count_write + '\n')
                file_names.append(f'{i}_exemple.txt')

        generate_files(count)

    else:
        print('Вы ввели неверное количество файлов')
        exit(1)

elif info == 'n':
    count = int(input('Сколько файлов будете использовать? (Файлы должны быть в 1 папке с программой) '))
    if 1 < count < 11:
        for i in range(count):
            file_i = input('Напишите название файла ')
            try:
                f = open(file_i, 'r')
                f.close()
            except FileNotFoundError:
                print(f'файл {file_i} не найден')
                exit(1)
            file_names.append(file_i)

    else:
        print('Вы ввели неверное количество файлов')
        exit(1)


def sort_single_file(file):
    """Сортируем числа в каждом файле"""
    # Создаем пустой список в который запишем числа из файла
    numbers = []
    with open(file, 'r') as f:
        # читаем из файла числа и записываем их в список пустой
        for line in f:
            num = int(line.strip())
            numbers.append(num)

    # Сортируем числа
    numbers.sort()
    # Записываем числа в отсортированном порядке в файл
    with open(file, 'w') as f:
        for i in numbers:
            f.write(str(i) + '\n')


def merge_files(input_files, output_file_finish):
    """Функция слияния файлов в 1"""
    # Записываем все файлы и берем у них индексы для кучи
    open_files = []
    for file in input_files:
        f = open(file, 'r')
        open_files.append(f)

    # Используем кучу и добавляем туда элемент и его индекс
    heap = []
    for index, file in enumerate(open_files):
        line = file.readline()
        if line:
            value = int(line.strip())
            heapq.heappush(heap, (value, index))

    # Делаем слияние файлов в 1 из кучи
    with open(output_file_finish, 'w') as f:
        while heap:
            value, index = heapq.heappop(heap)
            f.write(str(value) + '\n')
            next_line = open_files[index].readline()
            if next_line:
                heapq.heappush(heap, (int(next_line.strip()), index))

    # Закрываем все файлы
    for i in open_files:
        i.close()


# Используем функцию сортировки файлов
for i in file_names:
    sort_single_file(i)


# Из отсортированных файлов создаем выходной файл используя внешнюю сортировку слиянием
merge_files(file_names, output_file)