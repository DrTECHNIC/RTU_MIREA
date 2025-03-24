# Задание 3
def prac3_1():
    s = ["1", "2", "3"]
    print([int(i) for i in s])


def prac3_2():
    s = [1, 2, 2, 3, 3, 3]
    print(len(set(s)))


def prac3_3():
    s = [1, 2, 3, 4]
    print(s[::-1])


def prac3_4():
    s = [1, 3, 4, 5, 6, 4]
    x = 4
    print([i for i, val in enumerate(s) if val == x])


def prac3_5():
    s = [1, 2, 3, 4, 5, 7]
    print(sum(s[i] for i in range(0, len(s), 2)))


def prac3_6():
    s = ["12345", "qwerty", "wasd"]
    print(max(s, key=len))


def prac3_7():
    x = 24
    print(x % sum(map(int, str(x))) == 0)


def prac3_8():
    from itertools import groupby

    s = 'ABBCCCDEF'
    print([(k, len(list(g))) for k, g in groupby(s)])
    print([(k, sum(1 for _ in g)) for k, g in groupby(s)])


# Задание 4
def task4_1():
    A = [[0, 2], [3, 0]]
    B = [[1, 4], [2, 0]]

    def multiply(A, B):
        C = []
        for n in range(len(A)):
            ap = []
            for m in range(len(A[n])):
                ap.append(A[n][m] * B[n][m])
            C.append(ap)
        return C

    print(multiply(A, B))


def task4_2():
    A = [[0, 2, 1], [1, 0, 3], [0, 1, 1]]

    def transpose(A):
        C = []
        for n in range(len(A)):
            ap = []
            for m in range(len(A[n])):
                ap.append(A[m][n])
            C.append(ap)
        return C

    print(transpose(A))


def task4_3():
    A = [[1, 2], [3, 4], [5, 6]]
    B = [[1, 2, 3], [4, 5, 6]]

    def dot(A, B):
        C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    print(dot(A, B))


# Задание 5
def task5_1():
    def generate_groups():
        array = []
        groups = ["ИВБО", "ИКБО", "ИМБО", "ИНБО"]
        for group in groups:
            if group == "ИВБО":
                append = []
                numbers = [10, 11, 12, 13, 20, 21, 22]
                for number in numbers:
                    append.append(group + '-' + str(number) + "-23")
                array.append(append)

            elif group == "ИКБО":
                append = []
                numbers = [10, 10, 11, 12, 13, 14, 15, 20, 21, 22, 24, 34,
                           40, 41, 42, 43, 50, 51, 52, 60, 61, 62, 63, 64,
                           65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76]
                flag = 1
                for number in numbers:
                    if number == 10 and flag == 1 or number == 24 or number == 34:
                        append.append(group + '-' + str(number) + "-22")
                        flag = 0
                    else:
                        append.append(group + '-' + str(number) + "-23")
                array.append(append)

            elif group == "ИМБО":
                append = []
                numbers = [10, 11]
                for number in numbers:
                    append.append(group + '-' + str(number) + "-23")
                array.append(append)

            elif group == "ИНБО":
                append = []
                numbers = [10, 11, 12, 13, 20, 21, 22, 23, 30, 31, 32, 33]
                for number in numbers:
                    append.append(group + '-' + str(number) + "-23")
                array.append(append)

        return array

    list_of_groups = generate_groups()
    for i in list_of_groups:
        print('\n' + i[0][0:4] + ':')
        count = 0
        for j in i:
            print(j, end=" ")
            count += 1
            if count == 10:
                count = 0
                print()
        print()


def task5_2():
    import sys

    def Daniil_print(*objects, sep=' ', end='\n', file=sys.stdout):
        arg = [str(i) for i in objects]
        text = sep.join(arg) + end
        file.write(text)

    Daniil_print(123, "456")


def task5_3():
    from ctypes import c_uint32

    def encrypt(v, k):
        v0, v1 = c_uint32(v[0]), c_uint32(v[1])
        delta = 0x9e3779b9
        k0, k1, k2, k3 = k[0], k[1], k[2], k[3]
        total = c_uint32(0)
        for i in range(32):
            total.value += delta
            v0.value += ((v1.value << 4) + k0) ^ (v1.value + total.value) ^ ((v1.value >> 5) + k1)
            v1.value += ((v0.value << 4) + k2) ^ (v0.value + total.value) ^ ((v0.value >> 5) + k3)
        return v0.value, v1.value

    def decrypt(v, k):
        v0, v1 = c_uint32(v[0]), c_uint32(v[1])
        delta = 0x9e3779b9
        k0, k1, k2, k3 = k[0], k[1], k[2], k[3]
        total = c_uint32(delta * 32)
        for i in range(32):
            v1.value -= ((v0.value << 4) + k2) ^ (v0.value + total.value) ^ ((v0.value >> 5) + k3)
            v0.value -= ((v1.value << 4) + k0) ^ (v1.value + total.value) ^ ((v1.value >> 5) + k1)
            total.value -= delta
        return v0.value, v1.value

    def hex_to_uint32(hex_str):
        return int(hex_str, 16)

    e_message = [
        "E3238557", "6204A1F8", "E6537611", "174E5747",
        "5D954DA8", "8C2DFE97", "2911CB4C", "2CB7C66B",
        "E7F185A0", "C7E3FA40", "42419867", "374044DF",
        "2519F07D", "5A0C24D4", "F4A960C5", "31159418",
        "F2768EC7", "AEAF14CF", "071B2C95", "C9F22699",
        "FFB06F41", "2AC90051", "A53F035D", "830601A7",
        "EB475702", "183BAA6F", "12626744", "9B75A72F",
        "8DBFBFEC", "73C1A46E", "FFB06F41", "2AC90051",
        "97C5E4E9", "B1C26A21", "DD4A3463", "6B71162F",
        "8C075668", "7975D565", "6D95A700", "7272E637"
    ]
    key = [0, 4, 5, 1]
    e_data = [hex_to_uint32(i) for i in e_message]
    d_data = []
    for i in range(0, len(e_data), 2):
        e_block = [e_data[i], e_data[i + 1]]
        d_block = decrypt(e_block, key)
        d_data.append(d_block)
    for v0, v1 in d_data:
        print(f"{chr(v0)}{chr(v1)}", end='')


# Задание 7
def task7_1():
    rooms = {
        'room1': {
            'name': 'Комната №1',
            'description': 'Вы в начале лабиринта. Сможете ли из него выбраться?',
            'actions': [
                {
                    'text': 'Идти на север.',
                    'message': 'Вы углубляетессь в недры лабиринта...',
                    'next_label': 'room2'
                }
            ]
        },
        'room2': {
            'name': 'Комната №2',
            'description': 'Квадратная комната с красными стенами.',
            'actions': [
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы идёте в светлый проход...',
                    'next_label': 'room3'
                },
                {
                    'text': 'Идти на юг.',
                    'message': 'Вы поднимаетесь к светлой стартовой комнате...',
                    'next_label': 'room1'
                },
                {
                    'text': 'Идти на восток.',
                    'message': 'Вы идёте в тёмный проход...',
                    'next_label': 'room4'
                }
            ]
        },
        'room3': {
            'name': 'Комната №3',
            'description': 'Круглая комната с синими стенами.',
            'actions': [
                {
                    'text': 'Идти на юг.',
                    'message': 'Вы идёте по коридору, придающему уверенности в выборе...',
                    'next_label': 'room5'
                },
                {
                    'text': 'Идти на восток.',
                    'message': 'Вы идёте в комнату цвета мака...',
                    'next_label': 'room2'
                },
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы поднимаетесь по очень длинной летснице...',
                    'next_label': 'room6'
                }
            ]
        },
        'room4': {
            'name': 'Комната №4',
            'description': 'Квадратная комната с белыми стенами.',
            'actions': [
                {
                    'text': 'Идти на восток.',
                    'message': 'Вы поднимаетесь по не очень длинной лестнице...',
                    'next_label': 'room7'
                },
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы идёте по тёмному проходу...',
                    'next_label': 'room2'
                }
            ]
        },
        'room5': {
            'name': 'Комната №5',
            'description': 'Тупиковая комната',
            'actions': [
                {
                    'text': 'Идти на север.',
                    'message': 'Вы с грустью на душе возвращаетесь обратно',
                    'next_label': 'room3'
                }
            ]
        },
        'room6': {
            'name': 'Комната №6',
            'description': 'Комната с лифтом и числом "-5" на стене.',
            'actions': [
                {
                    'text': 'Идти на север.',
                    'message': 'Вы поднимаетесь вверх с помощью лифта...',
                    'next_label': 'room8'
                },
                {
                    'text': 'Идти на восток.',
                    'message': 'Вы спускаетесь по очень длинной летснице...',
                    'next_label': 'room3'
                }
            ]
        },
        'room7': {
            'name': 'Комната №7',
            'description': 'Круглая комната с красным полом и рисунком в виде белого кирпича',
            'actions': [
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы спускаетесь по не очень длинной лестнице...',
                    'next_label': 'room4'
                }
            ]
        },
        'room8': {
            'name': 'Комната №8',
            'description': 'Комната с лифтом и числом "1" на стене.',
            'actions': [
                {
                    'text': 'Идти на север.',
                    'message': 'Вы идёте в тёмную комнату...',
                    'next_label': 'room9'
                },
                {
                    'text': 'Идти на юг.',
                    'message': 'Вы спускаетесь вниз с помощью лифта...',
                    'next_label': 'room6'
                },
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы идёте в светлую комнату...',
                    'next_label': 'room10'
                }
            ]
        },
        'room9': {
            'name': 'Комната №9',
            'description': 'Тёмная комната.',
            'actions': [
                {
                    'text': 'Идти на юг.',
                    'message': 'Вы идёте в комнату с лифтом...',
                    'next_label': 'room8'
                },
                {
                    'text': 'Идти на юго-запад.',
                    'message': 'Вы идёте в светлую комнату',
                    'next_label': 'room10'
                }
            ]
        },
        'room10': {
            'name': 'Выход',
            'description': 'Вы нашли выход! Поздравляем!',
            'actions': []
        }
    }

    def play_game():
        current_label = 'room1'
        while True:
            current_room = rooms.get(current_label)
            if not current_room:
                print("Ошибка: комната не найдена.")
                break

            print("\n" + current_room['name'])
            print(current_room['description'])

            actions = current_room.get('actions', [])
            if not actions:
                print("\nКонец игры.")
                break

            for index, action in enumerate(actions, 1):
                print(f"{index}. {action['text']}")

            while True:
                choice = input("> ")
                try:
                    choice_index = int(choice) - 1
                    if 0 <= choice_index < len(actions):
                        selected_action = actions[choice_index]
                        break
                    else:
                        print("Неверный выбор. Попробуйте снова.")
                except ValueError:
                    print("Пожалуйста, введите номер.")

            if selected_action['message']:
                print(selected_action['message'])

            current_label = selected_action['next_label']

    play_game()


"""
digraph G {
    rankdir="UD";
    node [shape=box, style=filled, color=lightblue];

    // Комнаты (узлы)
    room1 [label="Комната №1\nВы в начале лабиринта. Сможете ли из него выбраться?"];
    room2 [label="Комната №2\nКвадратная комната с красными стенами."];
    room3 [label="Комната №3\nКруглая комната с синими стенами."];
    room4 [label="Комната №4\nКвадратная комната с белыми стенами."];
    room5 [label="Комната №5\nТупиковая комната"];
    room6 [label="Комната №6\nКомната с лифтом и числом \"-5\" на стене."];
    room7 [label="Комната №7\nКруглая комната с красным полом и рисунком в виде белого кирпича"];
    room8 [label="Комната №8\nКомната с лифтом и числом \"1\" на стене."];
    room9 [label="Комната №9\nТёмная комната."];
    room10 [label="Выход\nВы нашли выход! Поздравляем!"];

    // Переходы (рёбра)
    room1 -> room2 [label="Идти на север."];
    room2 -> room3 [label="Идти на запад."];
    room2 -> room1 [label="Идти на юг."];
    room2 -> room4 [label="Идти на восток."];
    room3 -> room5 [label="Идти на юг."];
    room3 -> room2 [label="Идти на восток."];
    room3 -> room6 [label="Идти на запад."];
    room4 -> room7 [label="Идти на восток."];
    room4 -> room2 [label="Идти на запад."];
    room5 -> room3 [label="Идти на север."];
    room6 -> room8 [label="Идти на север."];
    room6 -> room3 [label="Идти на восток."];
    room7 -> room4 [label="Идти на запад."];
    room8 -> room9 [label="Идти на север."];
    room8 -> room6 [label="Идти на юг."];
    room8 -> room10 [label="Идти на запад."];
    room9 -> room8 [label="Идти на юг."];
    room9 -> room10 [label="Идти на юго-запад."];
}"""

def task7_3():
    rooms = {
        'room1': {
            'name': 'Комната №1',
            'description': 'Вы в начале лабиринта. Сможете ли из него выбраться?',
            'actions': [
                {
                    'text': 'Идти на север.',
                    'message': 'Вы углубляетессь в недры лабиринта...',
                    'next_label': 'room2'
                }
            ]
        },
        'room2': {
            'name': 'Комната №2',
            'description': 'Квадратная комната с красными стенами.',
            'actions': [
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы идёте в светлый проход...',
                    'next_label': 'room3'
                },
                {
                    'text': 'Идти на юг.',
                    'message': 'Вы поднимаетесь к светлой стартовой комнате...',
                    'next_label': 'room1'
                },
                {
                    'text': 'Идти на восток.',
                    'message': 'Вы идёте в тёмный проход...',
                    'next_label': 'room4'
                }
            ]
        },
        'room3': {
            'name': 'Комната №3',
            'description': 'Круглая комната с синими стенами.',
            'actions': [
                {
                    'text': 'Идти на юг.',
                    'message': 'Вы идёте по коридору, придающему уверенности в выборе...',
                    'next_label': 'room5'
                },
                {
                    'text': 'Идти на восток.',
                    'message': 'Вы идёте в комнату цвета мака...',
                    'next_label': 'room2'
                },
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы поднимаетесь по очень длинной летснице...',
                    'next_label': 'room6'
                }
            ]
        },
        'room4': {
            'name': 'Комната №4',
            'description': 'Квадратная комната с белыми стенами.',
            'actions': [
                {
                    'text': 'Идти на восток.',
                    'message': 'Вы поднимаетесь по не очень длинной лестнице...',
                    'next_label': 'room7'
                },
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы идёте по тёмному проходу...',
                    'next_label': 'room2'
                }
            ]
        },
        'room5': {
            'name': 'Комната №5',
            'description': 'Тупиковая комната',
            'actions': [
                {
                    'text': 'Идти на север.',
                    'message': 'Вы с грустью на душе возвращаетесь обратно',
                    'next_label': 'room3'
                }
            ]
        },
        'room6': {
            'name': 'Комната №6',
            'description': 'Комната с лифтом и числом "-5" на стене.',
            'actions': [
                {
                    'text': 'Идти на север.',
                    'message': 'Вы поднимаетесь вверх с помощью лифта...',
                    'next_label': 'room8'
                },
                {
                    'text': 'Идти на восток.',
                    'message': 'Вы спускаетесь по очень длинной летснице...',
                    'next_label': 'room3'
                }
            ]
        },
        'room7': {
            'name': 'Комната №7',
            'description': 'Круглая комната с красным полом и рисунком в виде белого кирпича',
            'actions': [
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы спускаетесь по не очень длинной лестнице...',
                    'next_label': 'room4'
                }
            ]
        },
        'room8': {
            'name': 'Комната №8',
            'description': 'Комната с лифтом и числом "1" на стене.',
            'actions': [
                {
                    'text': 'Идти на север.',
                    'message': 'Вы идёте в тёмную комнату...',
                    'next_label': 'room9'
                },
                {
                    'text': 'Идти на юг.',
                    'message': 'Вы спускаетесь вниз с помощью лифта...',
                    'next_label': 'room6'
                },
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы идёте в светлую комнату...',
                    'next_label': 'room10'
                }
            ]
        },
        'room9': {
            'name': 'Комната №9',
            'description': 'Тёмная комната.',
            'actions': [
                {
                    'text': 'Идти на юг.',
                    'message': 'Вы идёте в комнату с лифтом...',
                    'next_label': 'room8'
                },
                {
                    'text': 'Идти на юго-запад.',
                    'message': 'Вы идёте в светлую комнату',
                    'next_label': 'room10'
                }
            ]
        },
        'room10': {
            'name': 'Выход',
            'description': 'Вы нашли выход! Поздравляем!',
            'actions': []
        }
    }

    from collections import deque
    from collections import defaultdict

    def find_dead_ends(rooms):
        reverse_graph = defaultdict(list)
        for room_label, room_info in rooms.items():
            for action in room_info['actions']:
                next_label = action['next_label']
                reverse_graph[next_label].append(room_label)
        visited = set()
        queue = deque()
        start_label = 'room10'
        if start_label in rooms:
            visited.add(start_label)
            queue.append(start_label)
        while queue:
            current_label = queue.popleft()
            for neighbor in reverse_graph.get(current_label, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        all_rooms = set(rooms.keys())
        unreachable = all_rooms - visited
        single_exit = [label for label in rooms if len(rooms[label]['actions']) == 1]
        dead_ends = unreachable.union(set(single_exit))
        dead_ends.discard('room10')
        return sorted(dead_ends)

    dead_ends = find_dead_ends(rooms)
    print("Найдены тупиковые комнаты:", dead_ends)


if __name__ == "__main__":
    task7_3()
