# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:

    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as cf:

        c = csv.DictReader(cf)
        data = list(c)

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as j:
        json.dump(data, j, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")