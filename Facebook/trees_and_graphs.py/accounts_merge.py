"""
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]


seen = set(0, 2, 1)
graph = {
    "johnsmith@mail.com": [],
    "john00@mail.com": [],
    "johnnybravo@mail.com": [],
    "john_newyork@mail.com":[],
    "mary@mail.com": []
}
(iterate)
[
    ["John",], 
    ["John", ], 
    ["John",], 
    ["Mary",]
]

name = John
emails = set("johnnybravo@mail.com")

[[John, h@mail.com", "john_newyork@mail.com"], [John, "johnnybravo@mail.com"], [mary, "mary@mail.com"]]

"""


from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        seen = set()
        graph = defaultdict(list)
        result = []
        #build graph with union
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                graph[accounts[i][j]].append(i)
        
        def dfs(account, path):
            if account in seen:
                return
            seen.add(account)
            while accounts[account][1:]:
                email = accounts[account].pop()
                path.add(email)
                while graph[email]:
                    new_account = graph[email].pop()
                    dfs(new_account, path)

        for i in range(len(accounts)):
            if i in seen:
                continue
            name, emails = accounts[i][0], set()
            dfs(i, emails)
            result.append([name] + sorted(emails))
        return result