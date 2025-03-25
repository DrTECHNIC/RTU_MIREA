def task_2_1():
    import numpy as np
    import matplotlib.pyplot as plt

    def generate_symmetric_sprite():
        quadrant = np.random.randint(0, 2, (3, 3))
        sprite = np.zeros((5, 5), dtype=int)
        for i in range(3):
            left_part = quadrant[i]
            right_part = left_part[1::-1]
            sprite[i] = np.concatenate([left_part, right_part])
        sprite[3] = sprite[1]
        sprite[4] = sprite[0]
        return sprite

    sprite = generate_symmetric_sprite()
    plt.imshow(sprite, cmap='grey', vmin=0, vmax=1)
    plt.axis('off')
    plt.show()


def task_2_2():
    import numpy as np
    import matplotlib.pyplot as plt

    def generate_symmetric_sprite():
        quadrant = np.random.randint(0, 2, (3, 3))
        sprite = np.zeros((5, 5), dtype=int)
        for i in range(3):
            left = quadrant[i]
            right = left[1::-1]
            sprite[i] = np.concatenate([left, right])
        sprite[3] = sprite[1]
        sprite[4] = sprite[0]
        return sprite

    def generate_sprite_map(vertical_steps, horizontal_steps):
        sprite_height = 5
        sprite_width = 5
        map_height = vertical_steps[-1] + sprite_height
        map_width = horizontal_steps[-1] + sprite_width
        sprite_map = np.zeros((map_height, map_width), dtype=int)
        for y in vertical_steps:
            for x in horizontal_steps:
                sprite = generate_symmetric_sprite()
                sprite_map[y:y + sprite_height, x:x + sprite_width] = sprite
        return sprite_map

    vertical_steps = [0, 20, 40, 60, 80]
    horizontal_steps = [0, 25, 50, 75, 100, 125, 150, 175]
    sprite_map = generate_sprite_map(vertical_steps, horizontal_steps)
    plt.figure(figsize=(10, 5))
    plt.imshow(sprite_map, cmap='gray', vmin=0, vmax=1)
    plt.axis('off')
    plt.show()


def task_2_3():
    import numpy as np
    import matplotlib.pyplot as plt
    import random
    from matplotlib.colors import to_rgb

    def generate_random_binary_sprite(width, height):
        return np.random.randint(0, 2, size=(height, width))

    def apply_horizontal_symmetry(sprite):
        height, width = sprite.shape
        for i in range(height // 2):
            sprite[height - 1 - i, :] = sprite[i, :]
        return sprite

    def apply_vertical_symmetry(sprite):
        height, width = sprite.shape
        for j in range(width // 2):
            sprite[:, width - 1 - j] = sprite[:, j]
        return sprite

    def colorize_base(binary_base, color_palette):
        height, width = binary_base.shape
        colored_base = np.full((height, width, 3), fill_value=to_rgb('black'), dtype=float)
        for i in range(height):
            for j in range(width):
                if binary_base[i, j] == 1:
                    colored_base[i, j] = to_rgb(random.choice(color_palette))
        return colored_base

    def generate_colored_sprite(width, height, symmetry='none', color_palette=['#1D2B53', '#7E2553', '#008751']):
        if symmetry == 'vertical':
            base_width = (width + 1) // 2
            binary_base = generate_random_binary_sprite(base_width, height)
            colored_base = colorize_base(binary_base, color_palette)
            colored_sprite = np.zeros((height, width, 3), dtype=float)
            colored_sprite[:, :base_width] = colored_base
            for j in range(width // 2):
                colored_sprite[:, width - 1 - j] = colored_sprite[:, j]
        elif symmetry == 'horizontal':
            base_height = (height + 1) // 2
            binary_base = generate_random_binary_sprite(width, base_height)
            colored_base = colorize_base(binary_base, color_palette)
            colored_sprite = np.zeros((height, width, 3), dtype=float)
            colored_sprite[:base_height, :] = colored_base
            for i in range(height // 2):
                colored_sprite[height - 1 - i, :] = colored_sprite[i, :]
        elif symmetry == 'both':
            base_width = (width + 1) // 2
            base_height = (height + 1) // 2
            binary_base = generate_random_binary_sprite(base_width, base_height)
            colored_base = colorize_base(binary_base, color_palette)
            colored_sprite = np.zeros((height, width, 3), dtype=float)
            colored_sprite[:base_height, :base_width] = colored_base
            for j in range(width // 2):
                colored_sprite[:base_height, width - 1 - j] = colored_sprite[:base_height, j]
            for i in range(height // 2):
                colored_sprite[height - 1 - i, :] = colored_sprite[i, :]
        else:
            binary_sprite = generate_random_binary_sprite(width, height)
            colored_sprite = np.full((height, width, 3), fill_value=to_rgb('black'), dtype=float)
            for i in range(height):
                for j in range(width):
                    if binary_sprite[i, j] == 1:
                        colored_sprite[i, j] = to_rgb(random.choice(color_palette))
        return colored_sprite

    def generate_colored_sprite_sheet(num_sprites_x, num_sprites_y, sprite_width=8, sprite_height=8, symmetry='none',
                                      color_palette=['#1D2B53', '#7E2553', '#008751'], grid_color='black'):
        sprite_sheet_width = num_sprites_x * sprite_width + (num_sprites_x - 1)
        sprite_sheet_height = num_sprites_y * sprite_height + (num_sprites_y - 1)
        sprite_sheet = np.full((sprite_sheet_height, sprite_sheet_width, 3), fill_value=to_rgb(grid_color), dtype=float)
        for i in range(num_sprites_y):
            for j in range(num_sprites_x):
                sprite = generate_colored_sprite(sprite_width, sprite_height, symmetry, color_palette)
                start_x = j * (sprite_width + 1)
                end_x = start_x + sprite_width
                start_y = i * (sprite_height + 1)
                end_y = start_y + sprite_height
                sprite_sheet[start_y:end_y, start_x:end_x] = sprite
        return sprite_sheet

    PICO8_PALETTE = [
        '#1D2B53', '#7E2553', '#008751', '#AB5236', '#5F574F', '#C2C3C7', '#FFF1E8', '#FF004D',
        '#FFA300', '#FFEC27', '#00E436', '#29ADFF', '#83769C', '#FF77A8', '#FFCCAA'
    ]
    sprite_width = 8
    sprite_height = 8
    num_sprites_x = 15
    num_sprites_y = 7
    symmetry_type = 'both'
    sprite_grid = generate_colored_sprite_sheet(num_sprites_x, num_sprites_y, sprite_width, sprite_height,
                                                symmetry_type, PICO8_PALETTE, grid_color='black')
    plt.imshow(sprite_grid)
    plt.show()


def task_2_5():
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.collections import LineCollection

    def generate_attraction_points(n, width, height):
        return np.random.rand(n, 2) * [width, height]

    def absorb_points(nodes, points, dk):
        to_remove = []
        for i, point in enumerate(points):
            if np.min(np.linalg.norm(nodes - point, axis=1)) < dk:
                to_remove.append(i)
        return np.delete(points, to_remove, axis=0)

    def find_influence_sets(nodes, points, di):
        influence_sets = {i: [] for i in range(len(nodes))}
        for point in points:
            distances = np.linalg.norm(nodes - point, axis=1)
            closest_idx = np.argmin(distances)
            if distances[closest_idx] <= di:
                influence_sets[closest_idx].append(point)
        return influence_sets

    def grow_tree(attraction_points, initial_node, dk, di, D, steps):
        nodes = np.array([initial_node])
        segments = []
        points = np.copy(attraction_points)

        for _ in range(steps):
            # Шаг 2: Поглощение точек
            points = absorb_points(nodes, points, dk)
            if len(points) == 0:
                break

            # Шаг 3: Поиск множеств влияния
            influence_sets = find_influence_sets(nodes, points, di)

            # Шаг 4: Рост новых узлов
            new_nodes = []
            for idx, S_v in influence_sets.items():
                if S_v:
                    vectors = [(s - nodes[idx])/np.linalg.norm(s - nodes[idx]) for s in S_v]
                    n_vec = np.sum(vectors, axis=0)
                    if np.linalg.norm(n_vec) > 1e-6:
                        n_hat = n_vec / np.linalg.norm(n_vec)
                        new_node = nodes[idx] + n_hat * D
                        new_nodes.append(new_node)
                        segments.append([nodes[idx], new_node])

            if new_nodes:
                nodes = np.vstack([nodes, new_nodes])
            else:
                break

        return nodes, segments

    def plot_trees(trees):
        fig, ax = plt.subplots(figsize=(10, 6))
        for tree in trees:
            segments = tree['segments']
            lc = LineCollection(segments, colors='green', linewidths=1)
            ax.add_collection(lc)
        ax.autoscale()
        ax.set_aspect('equal')
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()

    def generate_initial_positions(num_trees, width, height, min_distance):
        positions = []
        zone_width = width / num_trees
        for i in range(num_trees):
            x = i * zone_width + zone_width / 2
            y = np.random.uniform(0, height / 4)
            positions.append([x, y])
        return positions

    # Параметры
    width, height = 400, 250
    n_points = 500
    num_trees = 1  # Количество деревьев
    min_distance = 20  # Минимальное расстояние между деревьями
    dk = 5
    di = 40
    D = 10
    steps = 100

    # Начальные позиции с учетом минимального расстояния
    initial_positions = generate_initial_positions(num_trees, width, height, min_distance)

    # Генерация
    trees = []
    for i in range(num_trees):
        # Определяем зону для каждого дерева
        zone_width = width / num_trees
        left = i * zone_width
        right = (i + 1) * zone_width
        zone_points = generate_attraction_points(n_points // num_trees, zone_width - min_distance, height)
        zone_points[:, 0] += left + min_distance / 2  # Сдвигаем точки в свою зону

        # Генерация дерева
        nodes, segments = grow_tree(zone_points, initial_positions[i], dk, di, D, steps)
        trees.append({'nodes': nodes, 'segments': segments})

    # Визуализация
    plot_trees(trees)


def task_2_6():
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.collections import LineCollection
    from matplotlib.patches import Circle


    def generate_attraction_points(n, width, height, min_y):
        points = np.random.rand(n, 2) * [width, height - min_y]  # Генерация точек выше min_y
        points[:, 1] += min_y
        return points


    def absorb_points(nodes, points, dk):
        to_remove = []
        for i, point in enumerate(points):
            if np.min(np.linalg.norm(nodes - point, axis=1)) < dk:
                to_remove.append(i)
        return np.delete(points, to_remove, axis=0)


    def find_influence_sets(nodes, points, di):
        influence_sets = {i: [] for i in range(len(nodes))}
        for point in points:
            distances = np.linalg.norm(nodes - point, axis=1)
            closest_idx = np.argmin(distances)
            if distances[closest_idx] <= di:
                influence_sets[closest_idx].append(point)
        return influence_sets


    def grow_tree(attraction_points, initial_node, dk, di, D, steps, trunk_length):
        initial_node = np.array(initial_node, dtype=float)

        # Создаем ствол
        trunk_end = initial_node + np.array([0, trunk_length])  # Вершина ствола
        nodes = np.array([initial_node, trunk_end])  # Начальные узлы: основание и вершина ствола
        segments = [[initial_node, trunk_end]]  # Сегмент ствола
        points = np.copy(attraction_points)

        for _ in range(steps):
            points = absorb_points(nodes, points, dk)
            if len(points) == 0:
                break

            influence_sets = find_influence_sets(nodes, points, di)

            new_nodes = []
            for idx, S_v in influence_sets.items():
                if S_v:
                    vectors = [(s - nodes[idx]) / np.linalg.norm(s - nodes[idx]) for s in S_v]
                    n_vec = np.sum(vectors, axis=0)
                    if np.linalg.norm(n_vec) > 1e-6:
                        n_hat = n_vec / np.linalg.norm(n_vec)
                        new_node = nodes[idx] + n_hat * D
                        new_nodes.append(new_node)
                        segments.append([nodes[idx], new_node])

            if new_nodes:
                nodes = np.vstack([nodes, new_nodes])
            else:
                break

        return nodes, segments


    def add_leaves(ax, segments, leaf_radius, leaf_probability, max_leaves_per_segment, min_distance_between_leaves, min_y=45):
        leaves = []  # Список для хранения позиций листьев
        for segment in segments:
            # Проверяем, что выше min_y
            if segment[0][1] >= min_y or segment[1][1] >= min_y:
                # Добавляем листья с нашей вероятностью
                if np.random.rand() < leaf_probability:
                    # Количество листьев на текущем сегменте
                    num_leaves = np.random.randint(1, max_leaves_per_segment + 1)
                    for _ in range(num_leaves):
                        t = np.random.uniform(0, 1)  # Случайная позиция вдоль сегмента
                        x = segment[0][0] + t * (segment[1][0] - segment[0][0])
                        y = segment[0][1] + t * (segment[1][1] - segment[0][1])
                        # Проверяем, что лист выше min_y и расстояние до других листьев
                        if y >= min_y and all(np.linalg.norm(np.array([x, y]) - np.array(leaf)) >= min_distance_between_leaves for leaf in leaves):
                            leaves.append((x, y))
                            # Добавление листа
                            leaf_circle = Circle((x, y), leaf_radius, color='green', alpha=0.5)
                            ax.add_patch(leaf_circle)


    def plot_trees(trees, leaf_radius=4, leaf_probability=0.3, max_leaves_per_segment=3, min_distance_between_leaves=10, min_y=45):
        fig, ax = plt.subplots(figsize=(10, 6))
        for tree in trees:
            segments = tree['segments']
            lc = LineCollection(segments, colors='brown', linewidths=2)  # Коричневые ветки
            ax.add_collection(lc)
            # Добавляем листья (только выше min_y)
            add_leaves(ax, segments, leaf_radius, leaf_probability, max_leaves_per_segment, min_distance_between_leaves, min_y)
        ax.autoscale()
        ax.set_aspect('equal')
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()


    def generate_initial_positions(num_trees, width, trunk_base_y):
        positions = []
        zone_width = width / num_trees
        for i in range(num_trees):
            x = i * zone_width + zone_width / 2
            y = trunk_base_y  # Основание ствола на высоте trunk_base_y
            positions.append([x, y])
        return positions


    # Параметры
    width, height = 400, 250
    n_points = 500
    num_trees = 3  # Количество деревьев
    min_distance = 50  # Минимальное расстояние между деревьями
    dk = 5
    di = 40
    D = 10
    steps = 100
    trunk_length = 45  # Длина ствола
    trunk_base_y = 35  # Высота основания ствола
    leaf_radius = 8  # Радиус листьев
    leaf_probability = 0.5  # Вероятность появления листьев на сегменте
    max_leaves_per_segment = 3  # Максимальное количество листьев на сегмент
    min_distance_between_leaves = 20  # Минимальное расстояние между листьями
    min_y_for_leaves = 75  # Минимальная высота для появления листьев

    # Начальные позиции с учетом минимального расстояния
    initial_positions = generate_initial_positions(num_trees, width, trunk_base_y)

    # Генерация
    trees = []
    for i in range(num_trees):
        # Определяем зону для каждого дерева
        zone_width = width / num_trees
        left = i * zone_width
        right = (i + 1) * zone_width
        zone_points = generate_attraction_points(n_points // num_trees, zone_width - min_distance, height, trunk_base_y + trunk_length)
        zone_points[:, 0] += left + min_distance / 2  # Сдвигаем точки в свою зону

        # Генерация дерева
        nodes, segments = grow_tree(zone_points, initial_positions[i], dk, di, D, steps, trunk_length)
        trees.append({'nodes': nodes, 'segments': segments})

    # Визуализация с листьями только выше min_y_for_leaves
    plot_trees(trees, leaf_radius, leaf_probability, max_leaves_per_segment, min_distance_between_leaves, min_y_for_leaves)


if __name__ == "__main__":
    task_2_7()
