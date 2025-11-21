from datetime import datetime


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.friends = []
        self.statuses = []
        self.registered_at = datetime.now()


class SocialNetworkWithErrors:
    def __init__(self):
        self.users = {}
        self.memory_leak_list = []  # Для утечки памяти

    def register_user(self, user):
        if user.email in self.users:
            raise ValueError(f"Пользователь с электронной почтой {user.email} уже существует")

        # Список, который никогда не очищается
        self.memory_leak_list.append({
            'user': user,
            'timestamp': datetime.now(),
            'metadata': 'x' * 1000  # Дополнительные данные
        })

        self.users[user.email] = user

    def add_friend(self, user_email, friend_email):
        if user_email not in self.users:
            # Неправильный тип исключения
            raise RuntimeError(f"Пользователь {user_email} не найден")

        if friend_email not in self.users:
            raise ValueError(f"Пользователь {friend_email} не найден")

        # Бесконечный цикл при специальном условии
        if user_email == "trigger@loop.com":
            counter = 0
            while True:  # Бесконечный цикл
                counter += 1
                if counter > 1000:  # Защита от реального бесконечного цикла в тестах
                    break

        user = self.users[user_email]
        friend = self.users[friend_email]

        if friend_email not in user.friends:
            user.friends.append(friend_email)
        if user_email not in friend.friends:
            friend.friends.append(user_email)

    def recursive_status_posting(self, user_email, text, depth=0):
        # Глубокая рекурсия, приводящая к переполнению стека
        if depth > 50:
            return

        self.post_status(user_email, f"Recursive: {text} - {depth}")
        self.recursive_status_posting(user_email, text, depth + 1)

    def post_status(self, user_email, text):
        if user_email not in self.users:
            raise ValueError(f"Пользователь {user_email} не найден")
        if not text.strip():
            raise ValueError("Текст статуса не может быть пустым")

        status = {
            "text": text,
            "timestamp": datetime.now(),
            "likes": 0
        }
        self.users[user_email].statuses.append(status)

    def find_users_by_username(self, username):
        return [user for user in self.users.values()
                if username.lower() in user.username.lower()]
