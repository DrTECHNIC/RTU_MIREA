def solution(prices: list[int]):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

def print_result(prices):
    print(f"""
Input: prices = {prices}
Output: {solution(prices)}""")

def main():
    print_result([7, 1, 5, 3, 6, 4])
    print_result([7, 6, 4, 3, 1])

if __name__ == '__main__':
    main()