# Задание 1

"""
SELECT a.id, a.title, a.text
FROM article a
LEFT JOIN comment c ON a.id = c.article_id
WHERE c.id IS NULL;
"""


# Задание 2

def calculate(work_time_data: list) -> dict:
    worker_info = dict()
    for item in work_time_data:
        info = item.split(' ')
        key = ' '.join(info[0: -1])
        if worker_info.get(key):
            worker_info[key].append(int(info[-1]))
        else:
            worker_info[key] = list()
            worker_info[key].append(int(info[-1]))

    for value in worker_info.values():
        _sum = {'sum': sum(value)}
        value.append(_sum)

    return worker_info


data = [
    'Андрей 9',
    'Василий 11',
    'Роман 7',
    'X Æ A-12 45',
    'Иван Петров 3',
    'Андрей 6',
    'Роман 11',
]

print(calculate(data))
