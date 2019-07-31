"""
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

combos = [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
                                           *
[1, 2, 5]
 *

i = 11
coin = 1


"""


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