# Самое популярное решение
"""from dataclasses import dataclass


@dataclass
class BitField:
    name: str
    shift: int
    bits: int


def main(fields):
    field_config = [
        BitField('S1', shift=0, bits=1),
        BitField('S2', shift=1, bits=3),
        BitField('S3', shift=4, bits=3),
        BitField('S4', shift=7, bits=3),
    ]

    result = 0
    for name, value in fields:
        config = next(c for c in field_config if c.name == name)
        max_val = (1 << config.bits) - 1
        if value > max_val:
            raise ValueError(f"{name} должно быть не больше {max_val}")
        result |= (value << config.shift)
    return result"""


# 2-е по популярности решение
"""def main(array):
    S1 = array[0][1]
    S2 = array[1][1] << 1
    S3 = array[2][1] << 4
    S4 = array[3][1] << 7
    result = S1 | S2 | S3 | S4
    return result"""


if __name__ == "__main__":
    print(">>> main([('S1', 0), ('S2', 1), ('S3', 7), ('S4', 5)])\n",
          main([('S1', 0), ('S2', 1), ('S3', 7), ('S4', 5)]), '\n')
    print(">>> main([('S1', 0), ('S2', 0), ('S3', 1), ('S4', 6)])\n",
          main([('S1', 0), ('S2', 0), ('S3', 1), ('S4', 6)]), '\n')
    print(">>> main([('S1', 1), ('S2', 3), ('S3', 3), ('S4', 6)])\n",
          main([('S1', 1), ('S2', 3), ('S3', 3), ('S4', 6)]), '\n')
    print(">>> main([('S1', 1), ('S2', 0), ('S3', 4), ('S4', 5)])\n",
          main([('S1', 1), ('S2', 0), ('S3', 4), ('S4', 5)]), '\n')
