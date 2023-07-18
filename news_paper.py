class NewspaperSubscription:
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices


def find_subscription_combinations_helper(subscriptions, budget, current_combination, index, result):
    if budget < 0:
        return

    if budget == 0:
        result.append(current_combination.copy())
        return

    for i in range(index, len(subscriptions)):
        subscription = subscriptions[i]
        for day in range(7):
            price = subscription.prices[day]
            if price <= budget:
                current_combination.append(subscription.name)
                find_subscription_combinations_helper(subscriptions, budget - price, current_combination, i, result)
                current_combination.pop()


def find_subscription_combinations(subscriptions, budget):
    result = []
    find_subscription_combinations_helper(subscriptions, budget, [], 0, result)
    return result


if __name__ == "__main__":
    # Define the newspaper subscriptions
    toi_subscription = NewspaperSubscription("TOI", [3, 3, 3, 3, 3, 5, 6])
    hindu_subscription = NewspaperSubscription("Hindu", [2.5, 2.5, 2.5, 2.5, 2.5, 4, 4])
    et_subscription = NewspaperSubscription("ET", [4, 4, 4, 4, 4, 4, 10])
    bm_subscription = NewspaperSubscription("BM", [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5])
    ht_subscription = NewspaperSubscription("HT", [2, 2, 2, 2, 2, 4, 4])

    subscriptions = [toi_subscription, hindu_subscription, et_subscription, bm_subscription, ht_subscription]

    # Example inputs
    weekly_budget_1 = 40
    weekly_budget_2 = 35

    # Find combinations
    combinations_1 = find_subscription_combinations(subscriptions, weekly_budget_1)
    combinations_2 = find_subscription_combinations(subscriptions, weekly_budget_2)

    # Output the results
    print("Possible combinations for weekly budget 40:")
    for combo in combinations_1:
        print(combo)

    print("\nPossible combinations for weekly budget 35:")
    for combo in combinations_2:
        print(combo)
