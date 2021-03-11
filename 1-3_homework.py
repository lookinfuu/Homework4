inpoint = ""
while inpoint.lower() != "выход":
    print("""Какую задачу будем решать?
    1. Cортировка списка пузырьковым методом.
    2. Определим, совпадают ли множества элементов списка.
    3. Определим частоту использования всех символов в тексте.
    Используйте "выход" - чтобы выйти.
    """)
    inpoint = input("Введите номер задачи: ")

    if inpoint == "1":
        print("Cортировка списка пузырьковым методом\nИспользуйте \"назад\" чтобы вернуться в главное меню")
        numbers = ""
        while True:
            numbers = input("Введите числа через пробел:")
            if numbers != "назад":
                list_numbers = list(numbers.split())
                try:
                    test_list = list_numbers
                    for i in test_list:
                        float(i)
                except:
                    print("Вы ввели недопустимые значения. Попробуйте снова.")
                    continue
                exit = True
                while exit:
                    for i in range(0, len(list_numbers) - 1):
                        if float(list_numbers[i]) > float(list_numbers[i + 1]):
                            list_numbers.insert(i + 2, list_numbers[i])
                            list_numbers.pop(i)
                        for a in range(0, len(list_numbers) - 1):
                            if float(list_numbers[a]) > float(list_numbers[a + 1]):
                                break
                            elif a == (len(list_numbers) - 2):
                                exit = False
                                break
                print(list_numbers)  
            else:
                break  

    elif inpoint == "2":
        print("Определим, совпадают ли множества элементов списка\n(Enter - чтобы вернуться в главное меню)")
        a = 1
        b = 1
        while a and b:
            a = input("Введите элементы первого списка:")
            if a:
                b = input("Введите элементы второго списка:")
                if b:
                    a = set(list(a))
                    b = set(list(b))
                    if a == b:
                        print("Множества элементов списка совпадают")
                    else:
                        print("Множества элементов списка не совпадают")
    elif inpoint == "3":
        print("Определим частоту использования всех символов в тексте\nИспользуйте \"назад\" чтобы вернуться в главное меню")
        a = ""
        while a != "назад":
            a = input("Введите текст (Enter - взять данные из файла):")
            if a != "назад":
                if not a:
                    road_to_file = input("Укажите путь к файлу:")
                    if road_to_file:
                        try:
                            datafile = open(road_to_file, 'rb')
                            a = datafile.read().decode('utf-8')
                        except PermissionError:
                            print("Недостаточно прав для работы с файлом.")
                            continue
                        except FileNotFoundError:
                            print("Неверный путь к файлу или такого файла не существует.")
                            continue
                        except:
                            print("Неизвестная ошибка")
                            continue
                    else:
                        print("Нет данных.")
                        continue
                d = {}
                for i in a:
                    if i in d:
                        d[i] += 1
                    else:
                        d[i] = 1
                print(d)
    elif inpoint.lower() == "выход":
        print("Увидимся...")
    else:
        print("Ошибка.")