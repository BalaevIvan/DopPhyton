# TODO Напишите функцию find_common_participants

def find_common_participants(first_group, second_group, ras=","):

    first = first_group.split(ras)
    second = second_group.split(ras)

    genera = list(set(first) & set(second))
    genera.sort()

    return genera




participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

itog1 = find_common_participants(participants_first_group, participants_second_group, "|")
print(f"Общие участники1: {itog1}")


# TODO Провеьте работу функции с разделителем отличным от запятой

papapa = "Иванов_Петров_Сидоров"
pypypy = "Петров_Сидоров_Смирнов"

itog2 = find_common_participants(papapa, pypypy, "_")
print(f"Общие участники2: {itog2}")


#data = "apple,orange,banana"
#fruits = data.split(',')
#print(fruits)  # ['apple', 'orange', 'banana']
#words = ['Hello', 'World', 'Python']
#result = ' '.join(words)
#print(result)  # Hello World Python
#set_ = {1, 2, 3, 4, 5}
#list_ = [4, 5, 6, 7, 8]
#intersection_set = set_.intersection(list_)
#print(intersection_set)  # {4, 5}