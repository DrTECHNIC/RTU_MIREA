import unittest
from social_network import User, SocialNetwork


class TestSocialNetworkTDD(unittest.TestCase):

    def setUp(self):
        self.network = SocialNetwork()
        self.user1 = User("ivan", "ivan@mail.com", "password123")
        self.user2 = User("maria", "maria@mail.com", "password456")

    def test_user_registration(self):
        self.network.register_user(self.user1)
        self.assertIn("ivan@mail.com", self.network.users)

    def test_duplicate_registration(self):
        self.network.register_user(self.user1)
        with self.assertRaises(ValueError):
            self.network.register_user(User("ivan2", "ivan@mail.com", "pass"))

    def test_post_status(self):
        self.network.register_user(self.user1)
        self.network.post_status("ivan@mail.com", "Мой первый пост!")
        ivan = self.network.users["ivan@mail.com"]
        self.assertEqual(len(ivan.statuses), 1)
        self.assertEqual(ivan.statuses[0]["text"], "Мой первый пост!")

    def test_find_users_by_username(self):
        self.network.register_user(self.user1)
        self.network.register_user(self.user2)

        found_users = self.network.find_users_by_username("ivan")
        self.assertEqual(len(found_users), 1)
        self.assertEqual(found_users[0].email, "ivan@mail.com")

    def test_find_users_partial_match(self):
        user3 = User("ivanov", "ivanov@mail.com", "pass")
        self.network.register_user(self.user1)
        self.network.register_user(user3)

        found_users = self.network.find_users_by_username("iva")
        self.assertEqual(len(found_users), 2)


if __name__ == "__main__":
    unittest.main()
