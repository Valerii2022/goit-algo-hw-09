import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]  
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count
    return result

def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]  
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

def compare_algorithms():
    amount = 4999 

    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time

    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time

    print("Жадібний алгоритм:")
    print("Результат:", greedy_result)
    print("Час виконання:", greedy_time)

    print("\nДинамічне програмування:")
    print("Результат:", dp_result)
    print("Час виконання:", dp_time)

if __name__ == "__main__":
    compare_algorithms()

