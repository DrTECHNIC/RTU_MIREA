from memory_profiler import profile
from social_network_with_errors_dynamic import SocialNetworkWithErrors, User


@profile
def test_memory_leak():
    network = SocialNetworkWithErrors()

    for i in range(1000):
        user = User(f"test_user_{i}", f"user_{i}@memoryleak.com", "password123")
        network.register_user(user)

    for i in range(500):
        if i < 250:
            network.add_friend(f"user_{0}@memoryleak.com", f"user_{i}@memoryleak.com")

    return network


@profile
def test_normal_memory_usage():
    from social_network_without_errors import SocialNetwork, User

    network = SocialNetwork()

    for i in range(1000):
        user = User(f"test_user_{i}", f"user_{i}@normal.com", "password123")
        network.register_user(user)

    for i in range(500):
        if i < 250:
            network.add_friend(f"user_{0}@normal.com", f"user_{i}@normal.com")

    return network


if __name__ == "__main__":
    print("=== Memory leak test ===")
    network_with_leak = test_memory_leak()
    print("\n=== Normal Memory Usage Test ===")
    network_normal = test_normal_memory_usage()
