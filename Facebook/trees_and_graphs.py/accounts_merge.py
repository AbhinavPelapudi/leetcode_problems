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