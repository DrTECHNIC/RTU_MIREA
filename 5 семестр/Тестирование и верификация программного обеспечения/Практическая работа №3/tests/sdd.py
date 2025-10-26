import unittest
from social_network import SocialNetwork, User


SPECIFICATIONS = {
    "registration": [
        {
            "input": {"username": "Петр", "email": "petr@mail.com", "password": "123456"},
            "expected": "success",
            "description": "Успешная регистрация пользователя Петр"
        },
        {
            "input": {"username": "Дубликат", "email": "ivan@mail.com", "password": "654321"},
            "expected": "error",
            "description": "Ошибка: электронная почта ivan@mail.com уже существует"
        }
    ],
    "friendship": [
        {
            "input": {"user_email": "ivan@mail.com", "friend_email": "maria@mail.com"},
            "expected": "success",
            "description": "Успешное добавление друга: Иван и Мария становятся взаимными друзьями"
        }
    ],
    "status": [
        {
            "input": {"user_email": "ivan@mail.com", "text": "Привет всем!"},
            "expected": "success",
            "description": "Успешная публикация статуса 'Привет всем!' пользователем Иван"
        }
    ]
}


class SpecificationTestsSDD(unittest.TestCase):
    def setUp(self):
        self.network = SocialNetwork()
        self.network.register_user(User("Иван", "ivan@mail.com", "123456"))
        self.network.register_user(User("Мария", "maria@mail.com", "qwerty"))

    def test_registration_examples(self):
        for spec in SPECIFICATIONS["registration"]:
            with self.subTest(description=spec["description"]):
                if spec["expected"] == "success":
                    user = User(**spec["input"])
                    self.network.register_user(user)
                    self.assertIn(spec["input"]["email"], self.network.users)
                else:
                    with self.assertRaises(ValueError):
                        user = User(**spec["input"])
                        self.network.register_user(user)

    def test_friendship_examples(self):
        for spec in SPECIFICATIONS["friendship"]:
            with self.subTest(description=spec["description"]):
                self.network.add_friend(**spec["input"])
                user = self.network.users[spec["input"]["user_email"]]
                friend = self.network.users[spec["input"]["friend_email"]]
                self.assertIn(spec["input"]["friend_email"], user.friends)
                self.assertIn(spec["input"]["user_email"], friend.friends)

    def test_status_examples(self):
        for spec in SPECIFICATIONS["status"]:
            with self.subTest(description=spec["description"]):
                self.network.post_status(**spec["input"])
                user = self.network.users[spec["input"]["user_email"]]
                self.assertEqual(len(user.statuses), 1)
                self.assertEqual(user.statuses[0]["text"], spec["input"]["text"])


if __name__ == "__main__":
    unittest.main()
