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
    return


def task_2_6():
    return


if __name__ == "__main__":
    task_2_3()
