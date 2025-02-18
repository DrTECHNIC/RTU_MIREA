import math
import tkinter as tk


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


def func(x, y):
    task4_ = 6

    # Задание 4.1
    if task4_ == 1:
        if 0.2 <= x <= 0.8 and 0.2 <= y <= 0.8:
            return 0, 0, 0
        else:
            return 1, 1, 1

    # Задание 4.2
    elif task4_ == 2:
        def smoothstep(edge0, edge1, x):
            t = max(0.0, min(1.0, (x - edge0) / (edge1 - edge0)))
            return t * t * (3.0 - 2.0 * t)

        r_red = 0.3
        r_green = 0.3
        blur_size = 0.25
        d_red = math.hypot(x - 0.52, y - 0.52)
        d_green = math.hypot(x - 0.48, y - 0.48)
        t_red = 1.0 - smoothstep(r_red - blur_size, r_red, d_red)
        t_green = 1.0 - smoothstep(r_green - blur_size, r_green, d_green)
        return t_red, t_green, 0

    # Задание 4.3
    elif task4_ == 3:
        cx, cy = 0.5, 0.5
        radius = 0.4
        mouth_angle = 30
        distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
        angle = math.degrees(math.atan2(y - cy, x - cx))
        if distance <= radius:
            if -mouth_angle <= angle <= mouth_angle:
                return 0, 0, 0
            else:
                eye_radius = 0.07
                eye_x, eye_y = 0.65, 0.25
                if ((x - eye_x) ** 2 + (y - eye_y) ** 2) <= eye_radius ** 2:
                    return 0, 0, 0
                return 1, 1, 0
        else:
            return 0, 0, 0

    # Задание 4.4
    elif task4_ == 4:
        def noise(x, y):
            return (math.sin(x * 12.9898 + y * 78.233) * 43758.5453) % 1
        total = noise(x, y)
        return total, total, total

    # Задание 4.5
    elif task4_ == 5:
        def noise(x, y):
            return (math.sin(x * 12.9898 + y * 78.233) * 43758.5453) % 1

        def val_noise(x, y):
            x0 = int(x)
            x1 = x0 + 1
            y0 = int(y)
            y1 = y0 + 1
            s = x - x0
            t = y - y0
            s = s * s * (3.0 - 2.0 * s)
            t = t * t * (3.0 - 2.0 * t)
            n00 = noise(x0, y0)
            n01 = noise(x0, y1)
            n10 = noise(x1, y0)
            n11 = noise(x1, y1)
            ix0 = n00 + (n10 - n00) * s
            ix1 = n01 + (n11 - n01) * s
            value = ix0 + (ix1 - ix0) * t
            return value

        scale = 15.0
        total = val_noise(x * scale, y * scale)
        return total, total, total

    # Задание 4.6
    elif task4_ == 6:
        def noise(x, y):
            return (math.sin(x * 12.9898 + y * 78.233) * 43758.5453) % 1

        def val_noise(x, y):
            x0 = int(x)
            y0 = int(y)
            x1 = x0 + 1
            y1 = y0 + 1
            s = x - x0
            t = y - y0
            s = s * s * (3.0 - 2.0 * s)
            t = t * t * (3.0 - 2.0 * t)
            n00 = noise(x0, y0)
            n01 = noise(x0, y1)
            n10 = noise(x1, y0)
            n11 = noise(x1, y1)
            ix0 = n00 + (n10 - n00) * s
            ix1 = n01 + (n11 - n01) * s
            value = ix0 + (ix1 - ix0) * t
            return value

        octaves = 5
        persistence = 0.5
        scale = 5.0
        total = 0.0
        amplitude = 1.0
        frequency = 1.0
        max_value = 0.0
        for _ in range(octaves):
            tx = x * scale * frequency
            ty = y * scale * frequency
            total += val_noise(tx, ty) * amplitude
            max_value += amplitude
            amplitude *= persistence
            frequency *= 2.0
        total /= max_value
        total = total ** 2
        return total, total, 255


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
