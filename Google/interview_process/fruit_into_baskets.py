# Fruit Into Baskets

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        fruit_types = {}
        total_fruit = max_fruit = 0 
        start = 0 
        for i in range(len(tree)):
            fruit_types[tree[i]] = fruit_types.get(tree[i], 0) + 1
            if len(fruit_types) > 2:
                while len(fruit_types) > 2:
                    fruit_types[tree[start]] -= 1
                    total_fruit -= 1
                    if not fruit_types[tree[start]]:
                        fruit_types.pop(tree[start])
                    start += 1
            total_fruit += 1
            if total_fruit > max_fruit:
                 max_fruit = total_fruit
        return max_fruit