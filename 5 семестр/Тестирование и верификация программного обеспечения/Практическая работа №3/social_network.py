from datetime import datetime


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.friends = []
        self.statuses = []
        self.registered_at = datetime.now()


class SocialNetwork:
    def __init__(self):
        self.users = {}

    def register_user(self, user):
        if user.email in self.users:
            raise ValueError(f"Пользователь с электронной почтой {user.email} уже существует")
        self.users[user.email] = user

    def add_friend(self, user_email, friend_email):
        if user_email not in self.users:
            raise ValueError(f"Пользователь {user_email} не найден")
        if friend_email not in self.users:
            raise ValueError(f"Пользователь {friend_email} не найден")
        if user_email == friend_email:
            raise ValueError("Нельзя добавить самого себя в друзья")
        user = self.users[user_email]
        friend = self.users[friend_email]
        if friend_email not in user.friends:
            user.friends.append(friend_email)
        if user_email not in friend.friends:
            friend.friends.append(user_email)

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

    # Для tdd
    def find_users_by_username(self, username):
        return [user for user in self.users.values() if username.lower() in user.username.lower()]
