print("Удалим из списка элементы, значения которых уже встречались в этом же списке в предыдущих элементах")
a = list(input("Введите элементы списка:"))
print(f'Список до удаления:{a}')
a = set(a)
print(f'Список после удаления:{a}')