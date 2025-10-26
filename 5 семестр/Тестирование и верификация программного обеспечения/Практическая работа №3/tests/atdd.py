import unittest
from social_network import SocialNetwork, User


class AcceptanceTestsATDD(unittest.TestCase):

    def test_friendship_flow(self):
        network = SocialNetwork()

        user1 = User("alice", "alice@mail.com", "pass1")
        user2 = User("bob", "bob@mail.com", "pass2")
        network.register_user(user1)
        network.register_user(user2)

        network.add_friend("alice@mail.com", "bob@mail.com")

        alice = network.users["alice@mail.com"]
        bob = network.users["bob@mail.com"]

        self.assertIn("bob@mail.com", alice.friends)
        self.assertIn("alice@mail.com", bob.friends)


if __name__ == "__main__":
    unittest.main()
