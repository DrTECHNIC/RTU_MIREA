def task2():
    import csv
    from datetime import datetime
    import matplotlib.pyplot as plt
    import numpy as np

    def parse_time(text):
        return datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')

    def load_csv(filename):
        with open(filename, encoding='utf8') as f:
            return list(csv.reader(f, delimiter=','))

    messages = load_csv('messages.csv')[1:]

    hours = [parse_time(row[4]).hour for row in messages]

    plt.figure(figsize=(12, 6))
    plt.hist(hours, bins=24, range=(0, 24), color='blue', edgecolor='black', alpha=1)

    plt.title('Активность студентов по времени суток', fontsize=14)
    plt.xlabel('Час дня', fontsize=12)
    plt.ylabel('Количество сообщений', fontsize=12)
    plt.xticks(np.arange(0, 24, 1))
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()


def task3():
    import csv
    from collections import defaultdict
    import matplotlib.pyplot as plt

    def load_csv(filename):
        with open(filename, encoding='utf8') as f:
            return list(csv.reader(f, delimiter=','))

    messages = load_csv('messages.csv')[1:]
    statuses = load_csv('statuses.csv')[1:]

    task_messages = defaultdict(int)
    for row in messages:
        task = row[1]
        task_messages[task] += 1

    task_students = defaultdict(set)
    for row in statuses:
        task, variant, group = row[0], row[1], row[2]
        task_students[task].add((variant, group))

    tasks = []
    averages = []
    for task in sorted(task_messages.keys(), key=lambda x: int(x) if x.isdigit() else x):
        if task in task_students and len(task_students[task]) > 0:
            avg = task_messages[task] / len(task_students[task])
            tasks.append(task)
            averages.append(avg)

    plt.figure(figsize=(12, 6))
    bars = plt.bar(tasks, averages, color='#4c72b0')

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height,
                 f'{height:.1f}',
                 ha='center', va='bottom')

    plt.title('Среднее количество сообщений по задачам', pad=20, fontsize=14)
    plt.xlabel('Номер задачи', labelpad=10)
    plt.ylabel('Сообщений на студента', labelpad=10)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()


def task4():
    import csv
    from datetime import datetime
    import matplotlib.pyplot as plt
    import pandas as pd
    from matplotlib.dates import DateFormatter

    def parse_time(text):
        return datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')

    def load_csv(filename):
        with open(filename, encoding='utf8') as f:
            return list(csv.reader(f, delimiter=','))

    messages = load_csv('messages.csv')[1:]
    statuses = load_csv('statuses.csv')[1:]

    df = pd.DataFrame(messages, columns=['id', 'task', 'variant', 'group', 'time'])
    df['time'] = df['time'].apply(parse_time)
    df['date'] = df['time'].dt.date

    activity = df.groupby(['date', 'task']).size().unstack().fillna(0)

    start_date = df['date'].min()
    end_date = df['date'].max()

    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    activity = activity.reindex(date_range.date, fill_value=0)

    plt.figure(figsize=(14, 8))

    for task in activity.columns:
        plt.plot(activity.index, activity[task], label=f'Задача {task}', marker='o', markersize=4)

    plt.title('Динамика активности студентов по задачам', pad=20, fontsize=14)
    plt.xlabel('Дата', labelpad=10)
    plt.ylabel('Количество сообщений', labelpad=10)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)

    date_form = DateFormatter("%Y-%m-%d")
    plt.gca().xaxis.set_major_formatter(date_form)

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()


def task5():
    import csv
    import matplotlib.pyplot as plt
    import pandas as pd

    def load_csv(filename):
        with open(filename, encoding='utf8') as f:
            return list(csv.reader(f, delimiter=','))

    messages = load_csv('messages.csv')[1:]
    groups = load_csv('groups.csv')[1:]

    df = pd.DataFrame(messages, columns=['id', 'task', 'variant', 'group', 'time'])
    group_counts = df['group'].value_counts().reset_index()
    group_counts.columns = ['group_id', 'message_count']

    group_names = pd.DataFrame(groups, columns=['id', 'title'])
    result = pd.merge(group_counts, group_names, left_on='group_id', right_on='id')
    result = result.sort_values('message_count', ascending=False)

    plt.figure(figsize=(12, 6))
    bars = plt.bar(result['title'], result['message_count'], color='#1f77b4')

    plt.title('Количество сообщений по группам')
    plt.xlabel('Группа')
    plt.ylabel('Количество сообщений')
    plt.xticks(rotation=45)
    plt.grid(axis='y')

    plt.tight_layout()
    plt.show()


def task6():
    import csv
    import matplotlib.pyplot as plt
    import pandas as pd

    def load_csv(filename):
        with open(filename, encoding='utf8') as f:
            return list(csv.reader(f, delimiter=','))

    statuses = load_csv('statuses.csv')[1:]
    groups = load_csv('groups.csv')[1:]

    df = pd.DataFrame(statuses, columns=['task', 'variant', 'group', 'time', 'status', 'achievements'])
    correct = df[df['status'] == '2']
    group_correct = correct['group'].value_counts().reset_index()
    group_correct.columns = ['group_id', 'correct_count']

    group_names = pd.DataFrame(groups, columns=['id', 'title'])
    result = pd.merge(group_correct, group_names, left_on='group_id', right_on='id')
    result = result.sort_values('correct_count', ascending=False)

    plt.figure(figsize=(12, 6))
    bars = plt.bar(result['title'], result['correct_count'], color='#2ca02c')

    plt.title('Количество правильных решений по группам')
    plt.xlabel('Группа')
    plt.ylabel('Правильные решения')
    plt.xticks(rotation=45)
    plt.grid(axis='y')

    plt.tight_layout()
    plt.show()


def task7():
    import csv
    import matplotlib.pyplot as plt
    import pandas as pd

    def load_csv(filename):
        with open(filename, encoding='utf8') as f:
            return list(csv.reader(f, delimiter=','))

    statuses = load_csv('statuses.csv')[1:]

    df = pd.DataFrame(statuses, columns=['task', 'variant', 'group', 'time', 'status', 'achievements'])
    df['status'] = df['status'].astype(int)
    task_stats = df.groupby('task')['status'].agg(['count', 'mean']).reset_index()
    task_stats = task_stats.sort_values('mean', ascending=False)

    plt.figure(figsize=(12, 6))
    plt.bar(task_stats['task'], task_stats['mean'], color='#ff7f0e')

    for i, row in task_stats.iterrows():
        plt.text(i, row['mean'] + 0.02, f"{row['mean']:.2f}", ha='center')

    plt.axhline(y=task_stats['mean'].mean(), color='r', linestyle='--')
    plt.title('Сложность задач (средний статус решения)')
    plt.xlabel('Задача')
    plt.ylabel('Средний статус (2=правильно)')
    plt.xticks(rotation=45)
    plt.grid(axis='y')

    plt.tight_layout()
    plt.show()

    print("Самые легкие задачи:", task_stats.head(3)['task'].tolist())
    print("Самые сложные задачи:", task_stats.tail(3)['task'].tolist())


def task8():
    import csv
    import matplotlib.pyplot as plt
    import pandas as pd

    def load_csv(filename):
        with open(filename, encoding='utf8') as f:
            return list(csv.reader(f, delimiter=','))

    statuses = load_csv('statuses.csv')[1:]
    groups = load_csv('groups.csv')[1:]

    df = pd.DataFrame(statuses, columns=['task', 'variant', 'group', 'time', 'status', 'achievements'])
    df['achievements'] = df['achievements'].apply(lambda x: len(x.split(',')) if x else 0)
    group_achievements = df.groupby('group')['achievements'].sum().reset_index()

    group_names = pd.DataFrame(groups, columns=['id', 'title'])
    result = pd.merge(group_achievements, group_names, left_on='group', right_on='id')
    result = result.sort_values('achievements', ascending=False)

    plt.figure(figsize=(14, 7))
    bars = plt.bar(result['title'], result['achievements'], color='#17becf')

    plt.title('Общее количество достижений по группам', fontsize=14, pad=20)
    plt.xlabel('Группа', fontsize=12)
    plt.ylabel('Количество достижений', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', alpha=0.4)

    plt.tight_layout()
    plt.show()


def task9():
    import csv
    import matplotlib.pyplot as plt
    import pandas as pd

    def load_csv(filename):
        with open(filename, encoding='utf8') as f:
            return list(csv.reader(f, delimiter=','))

    statuses = load_csv('statuses.csv')[1:]
    groups = load_csv('groups.csv')[1:]

    df_status = pd.DataFrame(statuses, columns=['task', 'variant', 'group', 'time', 'status', 'achievements'])
    df_status['achievements_count'] = df_status['achievements'].apply(lambda x: len(x.split(',')) if x else 0)
    df_status['status'] = pd.to_numeric(df_status['status'])

    student_stats = df_status.groupby(['variant', 'group']).agg(
        correct=('status', lambda x: (x == 2).sum()),
        achievements=('achievements_count', 'sum')
    ).reset_index()

    student_stats['score'] = student_stats['correct'] * 2 + student_stats['achievements']
    top_students = student_stats.sort_values('score', ascending=False).head(10)

    top_students = pd.merge(top_students, pd.DataFrame(groups, columns=['id', 'title']), left_on='group', right_on='id')
    top_students['student_name'] = 'Вариант ' + top_students['variant'] + ', ' + top_students['title']

    plt.figure(figsize=(10, 6))
    bars = plt.bar(top_students['student_name'], top_students['score'], color='lightblue')

    plt.title('Топ-10 студентов')
    plt.ylabel('Общий балл')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')

    plt.tight_layout()
    plt.show()


def task10():
    import csv
    import matplotlib.pyplot as plt
    import pandas as pd

    def load_csv(filename):
        with open(filename, encoding='utf8') as f:
            return list(csv.reader(f, delimiter=','))

    statuses = load_csv('statuses.csv')[1:]
    groups = load_csv('groups.csv')[1:]

    df = pd.DataFrame(statuses, columns=['task', 'variant', 'group', 'time', 'status', 'achievements'])
    df['unique_methods'] = df['achievements'].apply(lambda x: len(set(x.split(','))) if x else 0)
    group_methods = df.groupby('group')['unique_methods'].mean().reset_index()

    group_names = pd.DataFrame(groups, columns=['id', 'title'])
    result = pd.merge(group_methods, group_names, left_on='group', right_on='id')
    result = result.sort_values('unique_methods', ascending=False)

    plt.figure(figsize=(12, 6))
    plt.bar(result['title'], result['unique_methods'], color='purple')

    plt.title('Среднее количество различных способов решения по группам')
    plt.xlabel('Группа')
    plt.ylabel('Среднее число способов')
    plt.xticks(rotation=45)
    plt.grid(axis='y')

    plt.tight_layout()
    plt.show()


def task11():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('GAMES.csv', sep=';', header=None,
                     names=['title', 'genre', 'url', 'year'])

    df['year'] = df['year'].str.extract('(\d{4})').dropna().astype(int)

    year_counts = df['year'].value_counts().sort_index()

    plt.figure(figsize=(15, 6))
    year_counts.plot(kind='bar', color='#1f77b4', width=0.8)

    plt.title('Количество выпущенных игр по годам', fontsize=14, pad=20)
    plt.xlabel('Год выпуска', fontsize=12)
    plt.ylabel('Количество игр', fontsize=12)
    plt.xticks(rotation=90, fontsize=8)
    plt.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.show()


def task12():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('GAMES.csv', sep=';', header=None, names=['title', 'genre', 'url', 'year'])
    genre_counts = df['genre'].value_counts()

    plt.figure(figsize=(12, 6))
    genre_counts.plot(kind='bar', color='#4e79a7')

    plt.title('Количество игр по жанрам', fontsize=14)
    plt.xlabel('Жанр', fontsize=12)
    plt.ylabel('Количество игр', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    task8()
    task9()
    task10()
    task11()
    task12()
