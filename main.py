with open('files/recipe.txt', 'r', encoding='utf-8') as file_recipe:
    # Получаем из файла список рецептов
    all_recipe_list = file_recipe.readlines()
    cook_book = {}
    n = 0

    for i in all_recipe_list:
        lst = []
        tmp = []
        recipe_dct = {}
        #  Получаем название блюда
        dish = all_recipe_list[n].strip()
        n += 1
        #  Получаем число ингридиентов в блюде
        number = int(all_recipe_list[n].strip())
        n += 1
        #  Получаем список ингридиетов текущего блюда, создаем из него словарь и помещаем в список.
        for i in range(n, number + n):
            tmp = all_recipe_list[i].strip().split(' | ')
            recipe_dct['ingredient_name'] = tmp[0]
            recipe_dct['quantity'] = tmp[1]
            recipe_dct['measure'] = tmp[2]
            #  Копируем словарь, чтобы начальный использовать для следующего блюда
            recipe_dct1 = recipe_dct.copy()
            lst.append(recipe_dct1)
        #  Получаем словарь рецептов Название: рецепт
        cook_book[dish] = lst
        n += number + 1  # Пропускаем пустую строку после текущего рецепта
        if n >= len(all_recipe_list):
            break


# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    # Получаем список блюд и число персон. Считаем ингридиенты и количество
    out = {}
    ingr_list = []
    for dish in dishes:
        ingr_list = cook_book[dish]
        for i in ingr_list:
            ingredient_name = i['ingredient_name']
            if out.get(ingredient_name) is None:
                out[ingredient_name] = {'measure': i['measure'], 'quantity': int(i['quantity']) * person_count}
            else:
                out[ingredient_name]['quantity'] += int(i['quantity']) * person_count
    #        print(ingr_list)
    print(out)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
