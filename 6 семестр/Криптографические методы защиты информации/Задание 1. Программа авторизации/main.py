import random

def merkle_damgard_hash(password: str) -> int:
    data = password.encode('utf-8')
    bits = ''.join(f'{byte:08b}' for byte in data)
    blocks = []
    for i in range(0, len(bits), 16):
        block_bits = bits[i:i+16]
        if len(block_bits) < 16:
            block_bits = block_bits + '1' + '0' * (15 - len(block_bits))
        blocks.append(int(block_bits, 2))
    length_block = len(data) & 0xFFFF
    blocks.append(length_block)
    z = 0
    for block in blocks:
        z = (z ^ block) & 0xFFFF
    return z

def load_users():
    users = {}
    with open("users.txt", 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            parts = line.split('|')
            if len(parts) == 3:
                login, stored_str, salt_str = parts
                try: users[login] = (int(stored_str), int(salt_str))
                except ValueError: pass
    return users

def save_user(login, stored, salt):
    with open("users.txt", 'a', encoding='utf-8') as f:
        f.write(f"{login}|{stored}|{salt}\n")

def register(users):
    login = input("Логин: ").strip()
    if login in users:
        print("Ошибка: логин уже занят.")
        return
    password = input("Пароль (не менее 10 символов): ")
    if len(password) < 10:
        print("Ошибка: пароль должен содержать не менее 10 символов.")
        return
    hash = merkle_damgard_hash(password)
    salt = random.randrange(1024)
    stored = hash ^ salt
    users[login] = (stored, salt)
    save_user(login, stored, salt)
    print("Регистрация успешно завершена!")

def login(users):
    login = input("Логин: ").strip()
    if login not in users:
        print("Ошибка: пользователь с таким логином не найден.")
        return
    password = input("Пароль: ")
    h_input = merkle_damgard_hash(password)
    stored, salt = users[login]
    if (h_input ^ salt) == stored:
        print("Успешный вход!")
    else:
        print("Ошибка: неверный пароль.")

def main():
    users = load_users()
    while True:
        print()
        print("1. Регистрация")
        print("2. Вход")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()
        if choice == '1': register(users)
        elif choice == '2': login(users)
        elif choice == '0': break
        else: print("Неверный ввод.")

if __name__ == "__main__":
    main()
