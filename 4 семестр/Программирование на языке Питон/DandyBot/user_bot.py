def script(check, x, y):
    if check("gold", x, y) == 1:
        return "take"
    if check("level") == 1:
        if check("gold", x+1, y) == 1:
            return "right"
        if check("gold", x, y+1) == 1:
            return "down"
        return "right"
    if check("level") == 2:
        if check("gold", x, y-1) == 1:
            return "up"
        if check("gold", x+2, y) == 1:
            return "right"
        if check("gold", x+1, y) == 1:
            return "right"
        if check("gold", x, y+1) == 1:
            return "down"
        if check("gold", x+1, y-1) == 0:
            return "up"
        if check("gold", x+1, y-1) == 1:
            return "right"
    if check("level") == 3:
        # ЛЕВЫЙ НИЖНИЙ КВАДРАТ
        if x < 9 and y > 15:
            if check("wall", x+1, y) == 1:
                return "up"
            if check("wall", x, y+1) == 1:
                return "right"
            if check("wall", x-1, y) == 0 and check("wall", x, y+4) == 1:
                return "left"
            if check("wall", x-1, y) == 1 and check("wall", x, y-1) == 0:
                return "up"
            if check("wall", x+1, y) == 0:
                return "right"
        # ПРАВЫЙ НИЖНИЙ КВАДРАТ
        if x > 18 and y > 15:
            if check("gold", 19, 23) == 1:
                if check("wall", x, y+1) == 1:
                    return "left"
                if check("wall", x+1, y) == 0:
                    return "right"
                if check("wall", x+1, y) == 1:
                    return "down"
            if check("gold", 19, 23) == 0:
                return "up"
        # ПРАВЫЙ ВЕРХНИЙ КВАДРАТ
        if x > 18 and y < 9:
            if check("gold", 26, 8) == 1:
                if check("wall", x+1, y) == 1:
                    return "down"
                if check("wall", x, y-1) == 0:
                    return "up"
                if check("wall", x, y-1) == 1:
                    return "right"
            if check("gold", 26, 8) == 0:
                return "left"
        # ЛЕВЫЙ ВЕРХНИЙ КВАДРАТ
        if x < 9 and y < 9:
            if check("gold", 8, 1) == 1:
                if check("wall", x, y-1) == 1:
                    return "right"
                if check("wall", x-1, y) == 0:
                    return "left"
                if check("wall", x-1, y) == 1:
                    return "up"
            if check("gold", 8, 1) == 0:
                return "down"
        # ЦЕНТРАЛЬНЫЙ ПРЯМОУГОЛЬНИК
        if 7 < x < 20 and 7 < y < 17:
            if check("gold", x, y-1) == 1:
                return "up"
            if check("gold", x-1, y) == 1:
                return "left"
            if check("gold", x, y+1) == 1:
                return "down"
            if x == 8 and check("wall", x, y+1) == 0:
                return "down"
            if check("wall", x+1, y) == 1:
                return "up"
            if check("wall", x, y+1) == 1 and check("wall", x+2, y) == 1:
                return "right"
            if check("wall", x+1, y+1) == 1 or check("wall", x, y+1) == 1:
                return "right"
            if check("wall", x-1, y+1) == 1 or check("wall", x-1, y) == 1:
                return "down"
            if check("wall", x-1, y-1) == 1 or check("wall", x, y-1) == 1:
                return "left"
            if x == 19:
                return "up"
            if y == 16:
                return "right"
            if y == 8:
                return "left"
    if check("level") == 4:
        # ЛЕВЫЙ ВЕРХНИЙ КВАДРАТ
        if x < 9 and y < 9:
            if check("wall", x+1, y) == 1:
                return "down"
            if check("wall", x, y-1) == 1:
                return "right"
            return "right"
        # ПРАВЫЙ ВЕРХНИЙ КВАДРАТ
        if x > 18 and y < 9:
            if check("gold", 19, 8) == 1:
                if check("wall", x, y-7) == 0:
                    return "left"
                if check("wall", x+1, y) == 1:
                    return "down"
                if check("wall", x, y-1) == 0:
                    return "up"
                if check("wall", x, y-1) == 1:
                    return "right"
            if check("wall", x, y+1) == 1:
                return "right"
            return "down"
        # ЦЕНТРАЛЬНЫЙ ПРЯМОУГОЛЬНИК
        if 9 < x < 18 and 6 < y < 18:
            if check("gold", 17, 7) == 1:
                return "up"
            if check("gold", 10, 7) == 1:
                return "left"
            if check("gold", 10, 17) == 1:
                return "down"
            if check("gold", 17, 17) == 1:
                return "right"
            if check("wall", x+1, y) == 1:
                return "up"
            if check("wall", x+1, y+2) == 1:
                return "up"
            return "left"
        # ЛЕВЫЙ НИЖНИЙ КВАДРАТ
        if x < 9 and y > 15:
            if check("gold", 8, 16) == 1:
                if check("wall", x-7, y) == 0:
                    return "up"
                if check("wall", x, y+1) == 1:
                    return "right"
                if check("wall", x-1, y) == 0:
                    return "left"
                if check("wall", x-1, y) == 1:
                    return "down"
            if check("wall", x+1, y) == 1:
                return "down"
            return "right"
        # ПРАВЫЙ НИЖНИЙ КВАДРАТ
        if x > 18 and y > 15:
            if check("wall", x, y+7) == 0:
                return "left"
            if check("wall", x+1, y) == 1:
                return "up"
            if check("wall", x, y+1) == 0:
                return "down"
            if check("wall", x, y+1) == 1:
                return "right"
        # ОСТАЛЬНОЕ
        if check("wall", x, y+2) == 1:
            return "right"
        if check("wall", x-1, y) == 1:
            return "down"
        if check("wall", x-1, y) == 0:
            return "left"
    if check("level") == 5:
        moves = [ ('right', 1, 0), ('down', 0, 1), ('left', -1, 0), ('up', 0, -1) ]
        explored = set()
        to_explore = [(x, y, [])]
        explored.add((x, y))
        while to_explore:
            current_x, current_y, path = to_explore.pop(0)
            for move, delta_x, delta_y in moves:
                new_x = current_x + delta_x
                new_y = current_y + delta_y
                if (new_x, new_y) not in explored:
                    explored.add((new_x, new_y))
                    if check('wall', new_x, new_y):
                        continue
                    if check('player', new_x, new_y):
                        continue
                    if check('gold', new_x, new_y) > 0:
                        if path: return path[0]
                        else: return move
                    new_path = path.copy()
                    new_path.append(move)
                    to_explore.append((new_x, new_y, new_path))
        for move, delta_x, delta_y in moves:
            new_x = x + delta_x
            new_y = y + delta_y
            if not check('wall', new_x, new_y):
                return move
    return "pass"