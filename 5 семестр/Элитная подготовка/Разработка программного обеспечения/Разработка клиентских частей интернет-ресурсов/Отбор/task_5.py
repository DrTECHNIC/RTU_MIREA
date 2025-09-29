class RecentCounter:
    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.pop(0)
        return len(self.requests)

def print_result(res: list):
    print(f"Output: {res}")

def main():
    results = list()
    recentCounter = RecentCounter()
    results.append(recentCounter.ping(1))
    results.append(recentCounter.ping(100))
    results.append(recentCounter.ping(3001))
    results.append(recentCounter.ping(3002))
    del recentCounter
    print_result(results)

if __name__ == '__main__':
    main()