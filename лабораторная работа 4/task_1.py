# TODO решите задачу
import json

def task() -> float:

    with open('input.json', 'r') as f:
        i = json.load(f)

    ITOG = sum(item['score'] * item['weight'] for item in i)

    return round(ITOG, 3)

if __name__ == '__main__':
    print(task())
