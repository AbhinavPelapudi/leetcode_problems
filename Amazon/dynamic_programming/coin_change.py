class Solution:
    def coinChange(self, denominations: List[int], amount: int) -> int:
        combos = [amount + 1] * (amount + 1)
        combos[0] = 0
        for i in range(1, amount + 1):
            for coin in denominations:
                if i >= coin:
                    position = combos[i - coin]
                    combos[i] = min(combos[i], position + 1)
        return -1 if combos[-1] == amount + 1 else combos[-1]