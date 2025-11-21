import pytest
from social_network_without_errors import SocialNetwork, User
from social_network_with_errors_dynamic import SocialNetworkWithErrors


class TestSocialNetworkOriginal:
    def setup_method(self):
        self.network = SocialNetwork()
        self.user1 = User("ivan_petrov", "ivan@example.com", "password123")
        self.user2 = User("maria_ivanova", "maria@example.com", "qwerty")
        self.network.register_user(self.user1)
        self.network.register_user(self.user2)

    def test_register_user(self):
        user3 = User("alex_smith", "alex@example.com", "pass123")
        self.network.register_user(user3)
        assert "alex@example.com" in self.network.users

    def test_register_duplicate_user(self):
        with pytest.raises(ValueError):
            self.network.register_user(self.user1)

    def test_add_friend(self):
        self.network.add_friend("ivan@example.com", "maria@example.com")
        assert "maria@example.com" in self.user1.friends
        assert "ivan@example.com" in self.user2.friends

    def test_add_self_as_friend(self):
        with pytest.raises(ValueError):
            self.network.add_friend("ivan@example.com", "ivan@example.com")

    def test_post_status(self):
        self.network.post_status("ivan@example.com", "Привет, мир!")
        assert len(self.user1.statuses) == 1
        assert self.user1.statuses[0]["text"] == "Привет, мир!"

    def test_post_empty_status(self):
        with pytest.raises(ValueError):
            self.network.post_status("ivan@example.com", "   ")

    def test_find_users(self):
        found_users = self.network.find_users_by_username("ivan")
        assert len(found_users) == 1
        assert found_users[0].username == "ivan_petrov"


class TestSocialNetworkWithErrors:
    def setup_method(self):
        self.network = SocialNetworkWithErrors()
        self.user1 = User("ivan_petrov", "ivan@example.com", "password123")
        self.user2 = User("maria_ivanova", "maria@example.com", "qwerty")
        self.network.register_user(self.user1)
        self.network.register_user(self.user2)

    def test_memory_leak_creation(self):
        """Тест создания утечки памяти"""
        initial_users_count = len(self.network.memory_leak_list)
        for i in range(10):
            user = User(f"user{i}", f"user{i}@test.com", "pass")
            self.network.register_user(user)
        assert len(self.network.memory_leak_list) == initial_users_count + 10

    def test_wrong_exception_type(self):
        with pytest.raises(RuntimeError):
            self.network.add_friend("nonexistent@test.com", "maria@example.com")

    def test_recursive_method(self):
        try:
            self.network.recursive_status_posting("ivan@example.com", "test")
        except RecursionError:
            pytest.fail("RecursionError occurred - too deep recursion")
