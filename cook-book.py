from pprint import pprint

def prepare_dict(file_name: str) -> dict:
    result: dict = dict()

    with open(file_name, encoding='utf-8') as file:
        for line in file:
            recipe_name = line.strip()
            records_quantity = int(file.readline())
            food_list = []
            for food in range(records_quantity):
                ingridient_name, quantity, measure = file.readline().split('|')
                food_list.append({"ingridient_name": ingridient_name, "quantity": int(quantity), "measure": measure.strip()})
            result[recipe_name] = food_list
            file.readline()
    return result
result_dict = prepare_dict("recipes.txt")
#pprint(result_dict)

def get_shop_list_by_dishes(result_dict, dishes, person_count):
    shop_list_dict = {}
    for dish in dishes:
        if dish in result_dict.keys():
            for ingridients in result_dict[dish]:
                ingridients['quantity'] *= person_count
                if ingridients['ingridient_name'] in shop_list_dict:
                    shop_list_dict[ingridients['ingridient_name']]['quantity'] += int(ingridients['quantity'])
                elif ingridients['ingridient_name'] not in shop_list_dict:
                    shop_list_dict[ingridients['ingridient_name']] = {'quantity': int(ingridients['quantity']), 'measure': ingridients['measure']}
    return shop_list_dict

pprint(get_shop_list_by_dishes(result_dict, ['Запеченный картофель', 'Омлет'], 2))