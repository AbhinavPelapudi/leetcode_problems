class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_addresses = set()
        for email in emails:
            local, domain = email.split('@')
            local = "".join(local.split('+')[0].split('.'))
            full_email = local + '@' + domain
            unique_addresses.add(full_email)
        return len(unique_addresses)
        