# Самое популярное решение
"""def remove_duplicate_columns(table):
    if not table:
        return []
    transposed = list(zip(*table))
    seen = set()
    unique = []
    for col in transposed:
        col_tuple = tuple(col)
        if col_tuple not in seen:
            seen.add(col_tuple)
            unique.append(col)
    return [list(row) for row in zip(*unique)] if unique else []


def remove_empty_rows(table):
    return [row for row in table if any(cell is not None for cell in row)]


def split_column(table, column_index):
    if not table:
        return []

    def process_cell(cell):
        if cell is None:
            return (None, None)
        parts = cell.split('#', 1)
        return (parts[0], parts[1] if len(parts) > 1 else None)

    return [
        [part0, *row[:column_index], *row[column_index + 1:], part1]
        for row in table
        for (part0, part1) in [process_cell(row[column_index])]
    ]


def transform_cells(table):
    def process_cell(cell):
        if cell is None:
            return cell
        # Преобразование флагов
        if cell == 'Y':  # Исправлено с 'У' на 'Y'
            return 'Выполнено'
        if cell == 'N':
            return 'Не выполнено'
        # Преобразование дат
        if '/' in cell:
            return cell.replace('/', '.')
        # Очистка номеров (только если нет #)
        if '-' in cell and '#' not in cell:
            return cell.replace('-', '')
        return cell

    return [
        [process_cell(cell) for cell in row]
        for row in table
    ]


def transpose_table(table):
    if not table:
        return []
    transposed = list(zip(*table))
    return [list(row) for row in transposed]


def process_table(input_table):
    table = remove_duplicate_columns(input_table)
    table = remove_empty_rows(table)
    if table:
        table = split_column(table, 0)
    table = transform_cells(table)
    return transpose_table(table)


def main(input_table):
    return process_table(input_table)"""


# 2-е по популярности решение
# Наиболее близкое решение, но не оно:
"""def get_unique_columns(t):
    # return [list(r) for r in zip(*dict.fromkeys(zip(*t)))]
    return transpose_table(dict.fromkeys(zip(*t)))


def remove_empty_rows(t):
    return [r for r in t if any(c is not None for c in r)]


def split_column(t):
    return [[r[0].split('#')[0], r[1], r[0].split('#')[1]] for r in t]


def transform_1(c):
    return c.replace('-', '')


def transform_2(c):
    return c.replace('/', '.')


def transform_3(c):
    return 'Выполнено' if c == 'Y' else 'Не выполнено' if c == 'N' else c


def transform_cell(t):
    return [[transform_3(transform_2(transform_1(c))) for c in r] for r in t]


def transpose_table(t):
    return [list(r) for r in zip(*t)]


def main(t):
    return transpose_table(
        transform_cell(
            split_column(
                remove_empty_rows(
                    get_unique_columns(t)))))"""

# Тоже возможный вариант:
"""def get_unique_columns(t):
    return transpose_table(dict.fromkeys(zip(*t)))


def remove_empty_rows(t):
    return list(filter(bool, map(lambda r: list(filter(bool, r)), t)))


def split_column(t):
    return list(map(lambda r: [r[0].split('#')[0], r[1],
                               r[0].split('#')[1]], t))


def transform_1(c):
    return c.replace('-', '')


def transform_2(c):
    return c.replace('/', '.')


def transform_3(c):
    return 'Выполнено' if c == 'Y' else 'Не выполнено' if c == 'N' else c


def transform_cell(t):
    return list(map(lambda r:
                    list(map(lambda c:
                             transform_3(
                                 transform_2(
                                     transform_1(c))),
                             r)), t))


def transpose_table(t):
    return list(map(lambda *r: list(r), *t))


def main(t):
    return transpose_table(
        transform_cell(
            split_column(
                remove_empty_rows(
                    get_unique_columns(t)))))"""

# И ещё один:
"""def main(t):
    t = list(map(list, zip(*dict.fromkeys(zip(*t)))))
    t = list(filter(bool, [list(filter(bool, r)) for r in t]))
    t = [[f"{r[0][:3]}{r[0][4:7]}{r[0][8:12]}",
          f"{r[1][:2]}.{r[1][3:5]}.{r[1][6:]}",
          'Выполнено' if r[0][-1] == 'Y' else 'Не выполнено']
         for r in t]
    return list(map(list, zip(*t)))"""


if __name__ == "__main__":
    print("\nПример 1:")
    for row in main([
        ['372-914-4062#Y', '02/11/28', '02/11/28'],
        ['426-721-2059#N', '01/04/09', '01/04/09'],
        [None, None, None],
        [None, None, None],
        ['960-548-1413#N', '99/07/22', '99/07/22']
    ]): print(row)
    print("\nПример 2:")
    for row in main([
        ['920-544-0563#Y', '00/12/12', '00/12/12'],
        [None, None, None],
        [None, None, None],
        ['653-961-6427#Y', '04/07/20', '04/07/20'],
        ['313-501-6401#N', '01/02/10', '01/02/10']
    ]): print(row)
