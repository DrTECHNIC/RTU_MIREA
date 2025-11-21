from datetime import datetime


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.friends = []
        self.statuses = []
        self.registered_at = datetime.now()

    def get_profile_info(self) -> dict:
        return {
            'username': self.username,
            'email': self.email,
            'friend_count': len(self.friends),
            'status_count': len(self.statuses),
            'registered_at': self.registered_at
        }


class SocialNetwork:
    def __init__(self):
        self.users = {}

    def register_user(self, user) -> None:
        if user.email in self.users:
            raise ValueError(f"Пользователь с электронной почтой"
                             f" {user.email} уже существует")
        self.users[user.email] = user

    def add_friend(self, user_email, friend_email) -> None:
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

    def post_status(self, user_email, text) -> None:
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

    def find_users_by_username(self, username) -> list:
        return [user for user in self.users.values()
                if username.lower() in user.username.lower()]


if __name__ == "__main__":
    network = SocialNetwork()
    user1 = User("ivan_petrov", "ivan@example.com", "password123")
    user2 = User("maria_ivanova", "maria@example.com", "qwerty")
    network.register_user(user1)
    network.register_user(user2)
    network.add_friend("ivan@example.com", "maria@example.com")
    network.post_status("ivan@example.com", "Мой первый статус!")
    found_users = network.find_users_by_username("ivan")
    print(f"Найдено пользователей: {len(found_users)}")
