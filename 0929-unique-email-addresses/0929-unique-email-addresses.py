class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            emails[i] = emails[i].split("@")[0].replace(".", "") + "@" + emails[i].split("@")[1]
            emails[i] = emails[i].lower()
        seen = set()
        for i in emails:
            seen.add(i.split("@")[0].split("+")[0] + "@" + i.split("@")[1])
        return len(seen)
